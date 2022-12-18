from dataclasses import dataclass


@dataclass
class DataClassWeather:
    """Dataclass storing weather data for Pidgeonfeather."""

    weather_code: int
    temperature_c: float
    temperature_apparent_c: float
    wind_speed_k: int
    wind_direction: int
    sunrise: str
    sunset: str
    visability_m: int
    humidity: int
