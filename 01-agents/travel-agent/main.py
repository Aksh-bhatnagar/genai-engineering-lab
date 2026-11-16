from agent.agent import Agent
from tools.destinations import get_destinations
from tools.weather import get_weather

agent = Agent(
    instructions="You are a helpful Travel assistant.",
    tools=[
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
    ],
    tools_function={
        "get_destinations": get_destinations,
        "get_weather": get_weather
    }
)

try:
    response = agent.run(
        "I want to travel to Japan. Tell me the available destinations, check the current weather in Tokyo, and then suggest which destination I should consider based on the weather."
    )

    print(response)

except Exception as e:
    print("Error:", e)