# WeatherDialog.py
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

"""Class to display a weather report dialog"""
import sys
#from PySide6.QtCore import *
#from PySide6.QtGui import *
from PySide6.QtWidgets import QDialog
import ui_weather


class WeatherDialog(QDialog, ui_weather.Ui_Weather):
    """Displays a weather dialog, inherits class generated from pyuic"""

    def __init__(self, parent=None):
        super(WeatherDialog, self).__init__(parent)

        # Set up the application
        self.setup()

    def setup(self):
        """Setup and start the application"""
        super(WeatherDialog, self).setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = WeatherDialog()
    main.show()
    app.exec_()
