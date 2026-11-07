from agent.agent import TravelAgent


agent = TravelAgent()


try:
    response = agent.run(
        "I want to travel to Japan. Tell me the available destinations, check the current weather in Tokyo, and then suggest which destination I should consider based on the weather."
    )

    print(response)

except Exception as e:
    print("Error:", e)