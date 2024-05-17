from typing import Annotated
import httpx
import os


def get_current_weather(
    lat: Annotated[float, "Latitude of the weather location"],
    lon: Annotated[float, "Longitude of the weather location"],
) -> dict:

    api_key = os.getenv("WEATHER_API_KEY")
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    arguments = f"?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    endpoint = f"{base_url}{arguments}"

    response = httpx.get(endpoint)

    json = response.json()
    print(json["coord"])

    return response.json()
