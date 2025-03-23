from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import httpx
import os
import json
import asyncio

load_dotenv()

# initialize server
mcp = FastMCP("tech_news")

USER_AGENT = "weather-app/1.0"

SITE = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("WEATHER_API_KEY")

async def Fetch_weather_info(city: str):
    """ It pulls the latest weather reports from the OpenWeatherMap API. """

    url = f"{SITE}?q={city}&appid={API_KEY}&units=metric"
    print("Hello from weather-mcp-server!")
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers={"User-Agent": USER_AGENT})
            response.raise_for_status()
            weather_data = response.json()
            
            if weather_data:
                return {
                    "city": weather_data["name"],
                    "country": weather_data["sys"]["country"],
                    "temperature": weather_data["main"]["temp"],
                    "description": weather_data["weather"][0]["description"],
                    "humidity": weather_data["main"]["humidity"],
                    "wind_speed": weather_data["wind"]["speed"],
                    "sunrise": weather_data["sys"]["sunrise"],
                    "sunset": weather_data["sys"]["sunset"],
                }
            return None
        except httpx.HTTPError as e:
            print(f"Error fetching weather data: {e}")
            return None

# # Proper way to run async function
# if __name__ == "__main__":
#     print(asyncio.run(Fetch_weather_info("karachi")))


@mcp.tool()
async def weather(city: str):
    """ It fetches the latest weather reports for the given city. 
    Args:
        city (str): The city name for which weather reports are required.
    Returns:
        dict: The weather reports for the given city.
    """

    weather_data = await Fetch_weather_info(city)
    if weather_data:
        return json.dumps(weather_data)
    return None



if __name__ == "__main__":
    mcp.run(transport="stdio")


