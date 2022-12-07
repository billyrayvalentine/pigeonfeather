# Abstract base class for PidgeonFeatherAbstractWeatherGetter

from abc import ABCMeta, abstractmethod

class PidgeonFeatherAbstractWeatherGetter(metaclass=ABCMeta):

    @abstractmethod
    def get_weather(latitude: float, longitude: float) -> dict:
        """Return a dictionary in the following format

        a = {}
        a["temperature_c"] = 10 # Int
        a["wind_speed"] = KM/s Int
        a["wind_direction"] = 0-360 Int
        a["weather_code"] = 0-99 Int"""
        pass


