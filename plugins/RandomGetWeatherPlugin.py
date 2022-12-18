# Implementation of ABCGetWeatherPlugin
# Return some random but valid weather data
from random import randint
from ABCGetWeatherPlugin import ABCGetWeatherPlugin
from DataClassWeather import DataClassWeather

class RandomGetWeatherPlugin(ABCGetWeatherPlugin):

    def get_weather(self, latitude: float, longitude: float) -> DataClassWeather:
        
        a = dict()
        a["weather_code"] = randint(0,99)
        a["temperature_c"] = randint(-50,50)
        a["temperature_apparent_c"] = randint(-50,50)
        a["wind_speed_k"] = randint(0,100)
        a["wind_direction"] = randint(0,360)
        a["sunrise"] = f"{randint(0,23)}:{randint(0,23)}"
        a["sunset"] = f"{randint(0,23)}:{randint(0,23)}"
        a["visability_m"] = randint(0,42)
        a["humidity"] = randint(0,100)
        b = DataClassWeather(**a)
        return b

if __name__ == "__main__":
    a = RandomGetWeatherPlugin()
    weather_data = a.get_weather(1,2)
    print(f"got: {weather_data}")
