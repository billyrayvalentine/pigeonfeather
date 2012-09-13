# GetWeather.py
# Copyright 2010 Ben Sampson (pigeonfeather@cerium.org)
# This file is part of Pigeon Feather (code.google.com/p/pigeonfeather)
#
# Pigeon Feather is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or any later
# version.
#
# Pigeon Feather is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License
# along with Pigeon Feather.  If not, see <http://www.gnu.org/licenses/>.

"""Function to get the weather for a given woeid and return in a dictionary"""
from urllib.parse import urlencode
from urllib.request import urlopen
from lxml import etree
from datetime import datetime


def getWeather(woeid, url='http://weather.yahooapis.com/forecastrss', \
    timeout=15):
    """Get the weather from Yahoo! weather service for a given WOEID
    and return a dictionary containing weather data.

    Keyword arguments:
        woeid -- A WOEID as defined in
            http://developer.yahoo.com/geo/geoplanet/guide/concepts.html
        url -- The URL to call for the API
        timeout -- The length in seconds before an exception is thrown

    Exceptions:
        IOError -- Is re-raised if caught from the call to urllib2
        IndexError -- Is re-raised if caught while try to parse the returned
            weather.  Usually thrown if weather data is invalid because of
            invalid woeid.

    Returns:
    A dictionary containg the weather information in this format

    fetched - a datetime object representing the time the weather was fetched
    city - e.g. Compton
    region - e.g. CA
    country - 'two-character country code' e.g. US

    windSpeedKph - Wind speed in Kilometers Per Hour
    windSpeedMph - Wind speed in Miles Per Hour
    chillF - Wind Chill in Fahrenheit
    chillC - Wind Chill in Celcius
    directionDegrees - Wind direction in degrees
    directionTextual - Wind direction as N, S, E, W

    humidity - humidy in percent e.g 90
    visibilityKm - Visibility in Kilometers
    visibilityMi - Visibility in Miles
    pressureIn - Atmospheric pressure in mercury
    pressureMb - Atmospheric pressure in millibars
    pressureTendancy - State of Barometric pressure, 'steady' | 'rising' | 'failing'

    code - yweather:forecast condition code e.g. 10
    tempF - Current temperature in Fahrenheit
    tempC - Current temperatyre in Celcius
    text - a textual description of conditions, for example, 'Partly Cloudy'

    sunrise - today's sunrise time in local time format of 'h:mm am/pm'
    sunset - today's sunset time in local time format of 'h:mm am/pm'
    """
    # Build the url. Always use the 'f' parameter for units as we convert
    # everything based on that.
    # If an exception is caught re-raise it
    params = urlencode({'u': 'f', 'w': woeid})
    getUrl = url + '?' + params
    #print(getUrl)

    try:
        f = urlopen(getUrl)
        data = f.read()
    except IOError as e:
        raise e

    # Build xml doc from returned data and get and return the code and temp
    # lxml could actually get the doc here
    tree = etree.fromstring(data)

    # Pull the weather data from the xml and keep it in a map to be returned
    weather = {}

    # fetched time
    weather['fetched'] = datetime.now()

    # Location data
    # Catch any exception caught here and re-raise beacuse of invalid data
    # Will usually happen in woeid is invalid
    try:
        location = tree.xpath('//y:location', \
            namespaces={'y': 'http://xml.weather.yahoo.com/ns/rss/1.0'})[0]
    except IndexError as ie:
        raise ie

    weather['city'] = location.get('city')
    weather['region'] = location.get('region')
    weather['country'] = location.get('country')

    # Wind Chill
    wind = tree.xpath('//y:wind', \
        namespaces={'y': 'http://xml.weather.yahoo.com/ns/rss/1.0'})[0]
    weather['chillF'] = wind.get('chill')
    weather['chillC'] = \
        int(round(((float(wind.get('chill')) - 32) / 9) * 5))

    # Wind Speed
    weather['windSpeedKph'] = int(round(float(wind.get('speed')) * 1.609344))
    weather['windSpeedMph'] = wind.get('speed')

    # Wind Direction
    weather['directionDegrees'] = wind.get('direction')

    # TODO - is this definitely right?
    # set a textual value for the direction
    direction = int(wind.get('direction'))
    if direction >= 0 and direction < 45:
        direction = 'N'
    elif direction >= 45 and direction < 90:
        direction = 'NE'
    elif direction >= 90 and direction < 135:
        direction = 'E'
    elif direction >= 135 and direction < 180:
        direction = 'SE'
    elif direction >= 180 and direction < 225:
        direction = 'S'
    elif direction >= 225 and direction < 270:
        direction = 'SW'
    elif direction >= 270 and direction < 315:
        direction = 'W'
    elif direction >= 315 and direction < 360:
        direction = 'NW'
    else:
        direction = 'N'

    weather['directionTextual'] = str(direction)

    # Humidity, Visibility and Pressure
    atmosphere = tree.xpath('//y:atmosphere', \
        namespaces={'y': 'http://xml.weather.yahoo.com/ns/rss/1.0'})[0]
    weather['humidity'] = atmosphere.get('humidity')
    weather['visibilityMi'] = atmosphere.get('visibility')
    weather['visibilityKm'] = \
        int(round(float(atmosphere.get('visibility')) * 1.609344))
    weather['pressureIn'] = atmosphere.get('pressure')
    weather['pressureMb'] = \
        str(round((float(atmosphere.get('pressure')) * 33.8637526),2))

    # Set a textual value for rising
    rising = int(atmosphere.get('rising'))
    if rising == 0:
        rising = 'steady'
    elif rising == 1:
        rising = 'rising'
    elif rising == 2:
        rising = 'falling'

    weather['pressureTendancy'] = str(rising)

    # Weather condition code, temperature, summary text
    condition = tree.xpath('//y:condition', \
        namespaces={'y': 'http://xml.weather.yahoo.com/ns/rss/1.0'})[0]
    weather['code'] = condition.get('code')
    weather['tempF'] = condition.get('temp')
    weather['tempC'] = \
        int(round(((float(condition.get('temp')) - 32) / 9) * 5))
    weather['text'] = condition.get('text')

    # Sunset and sunrise
    sun = tree.xpath('//y:astronomy', \
        namespaces={'y': 'http://xml.weather.yahoo.com/ns/rss/1.0'})[0]
    weather['sunrise'] = sun.get('sunrise')
    weather['sunset'] = sun.get('sunset')

    print(weather)
    return weather

if __name__ == '__main__':
    a = getWeather('44481', 'http://weather.yahooapis.com/forecastrss')
