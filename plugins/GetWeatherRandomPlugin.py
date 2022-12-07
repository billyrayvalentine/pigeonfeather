# Implementation of PidgeonFeatherAbstractWeatherGetter
# Return some random but valid weather data
from random import randint
from PidgeonFeatherAbstractWeatherGetter import PidgeonFeatherAbstractWeatherGetter

class PidgeonFeatherRandomWeatherGetter(PidgeonFeatherAbstractWeatherGetter):

    def get_weather(self, latitude: float, longitude: float) -> dict:
        a = dict()
        a["temperature_c"] = randint(-50,50)
        a["wind_speed"] = randint(0,100)
        a["wind_direction"] = randint(0,360)
        a["weather_code"] = randint(1,99)
        return a

if __name__ == "__main__":
    a = PidgeonFeatherRandomWeatherGetter()
    weather_data = a.get_weather(1,2)
    print(f"got: {weather_data}")
