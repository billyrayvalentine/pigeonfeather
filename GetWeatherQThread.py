# GetWeatherQThread.py
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

"""QThread subclass used in PigeonFeather for calling getWeather
and emitting a signal everytime there is an update
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from GetWeather import getWeather
import sys


class GetWeatherQThread(QThread):
    """Threaded version of getWeather.  Inherits QThread"""

    def __init__(self, woeid, updateTime=30, parent=None):
        """Set some class properties and call parent class init

        Keyword arguments:
        woeid -- Yahoo! locationID for weather
        updateTime -- how often the thread should get the weather
        """
        QThread.__init__(self, parent)
        self.woeid = woeid
        self.updateTime = updateTime

    def setWoeid(self, woeid):
        """Set the Yahoo! Location ID

        Keyword Arguments:
        weoid -- The woeid to use
        """
        self.woeid = woeid

    def run(self):
        """Call the getWeather function, emit WeatherUpdate signal
        with weather data, and sleep for the updateTime
        """
        while 1:
            print('Starting thread')
            print(self.woeid)
            try:
                res = getWeather(self.woeid)
            except IOError as e:
                # If we catch an error then wait and try again
                print('Get weather failed, trying again')
                self.sleep(self.updateTime)
                continue
            except IndexError as ie:
                # Catching a Index exception usually means the Xpath failed
                # because the WOEID was invalid, emit a 'WeatherReadError'
                # wait (so that the user might change the woeid) and try again
                print('Weather failed to be processed correctly, emiting a')
                print('WeatherReadError and trying again')
                msg = 'The weather could not be read.  Please check the Woeid'
                self.emit(SIGNAL('WeatherReadError'), msg)
                self.sleep(self.updateTime)
                continue

            # Weather was received ok emit the signal cotaining the dictionary
            self.emit(SIGNAL('WeatherUpdate'), res)
            self.sleep(self.updateTime)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = GetWeatherQThread('44481').start()
    app.exec_()
