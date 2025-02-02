from pydantic import BaseModel, Field
from openai import OpenAI
from enum import Enum

client = OpenAI()


class WeatherCondition(str, Enum):
    clear = "clear"
    cloudy = "cloudy"
    overcast = "overcast"


class Weather(BaseModel):
    """Weather forecast for a specific location."""

    city: str = Field(..., description="The name of the city.")
    temperature: int = Field(..., description="The temperature in degrees Celsius.")
    condition: WeatherCondition = Field(
        ..., description="The weather condition in simple language."
    )
    humidity: int = Field(..., description="Humidity in percentage")
    windspeed: int = Field(..., description="Wind speed in km/h")


info_strings = [
    "Good morning! The weather in New York today is cloudy with a temperature of 12°C. Humidity levels are at 72%, and winds are blowing at 15 km/h. Be prepared for a cool and overcast day—dress accordingly",
    "Hey there, New Yorkers! It's a cloudy day with temperatures at 12°C. Humidity is at 72%, and there’s a light breeze at 15 km/h. Perfect weather for a cozy coffee run—stay warm!",
    "The skies over New York are wrapped in a thick blanket of clouds! At 12°C with 72% humidity and winds at 15 km/h, it’s a crisp and breezy day. Will the sun break through, or will the clouds reign supreme? Stay tuned!",
    "New York, it looks like the sun hit snooze today! It’s a cool 12°C, pretty humid at 72%, and the wind is taking a casual stroll at 15 km/h. Grab a jacket and maybe some coffee—because the sky sure isn’t bringing the warmth!",
]

for info_str in info_strings:
    completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {"role": "user", "content": info_str},
        ],
        response_format=Weather,
    )

    response = completion.choices[0].message.parsed
    print(info_str, response, "", sep="\n")
