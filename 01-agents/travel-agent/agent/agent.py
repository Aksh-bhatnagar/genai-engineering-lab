import os
import json
from pyexpat.errors import messages
from urllib import response
from dotenv import load_dotenv
from openai import OpenAI

from tools.destinations import get_destinations
from tools.weather import get_weather


load_dotenv("../../.env")


class TravelAgent:

    def __init__(self):
        api_key = os.getenv("OPENROUTER_API_KEY")

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key
        )

        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_destinations",
                    "description": "Get a list of available travel destinations in a country.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "country": {
                                "type": "string",
                                "description": "The country to search destinations in."
                            }
                        },
                        "required": ["country"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_weather",
                    "description": "Get the current weather for a specific city.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "city": {
                                "type": "string",
                                "description": "The city to get weather information for."
                            }
                        },
                        "required": ["city"]
                    }
                }
            }
        ]

        self.tool_functions = {
            "get_destinations": get_destinations,
            "get_weather": get_weather
        }

    def run(self, user_message):

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a helpful travel agent. "
                    "Use the available tools when you need destination or weather information. "
                    "Never invent tool results."
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]

        MAX_ITERATIONS = 5
        for _ in range(MAX_ITERATIONS):
            response = self.client.chat.completions.create(
                model="openrouter/free",
                messages=messages,
                tools=self.tools
            )

            message = response.choices[0].message

            messages.append(message)

            # No tool call means the agent has reached its final answer
            if not message.tool_calls:
                return message.content

            # Execute every tool requested by the LLM
            for tool_call in message.tool_calls:

                function_name = tool_call.function.name

                arguments = json.loads(
                    tool_call.function.arguments
                )

                function = self.tool_functions.get(function_name)

                if not function:
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": f"Error: Unknown tool '{function_name}'."
                    })
                    continue

                try:
                    result = function(**arguments)
                except Exception as e:
                    result = f"Error executing tool '{function_name}': {str(e)}"

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                    })

        return "The agent reached its maximum number of iterations."