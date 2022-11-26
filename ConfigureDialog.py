# ConfigureDialog.py
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

"""Class to display a configure report dialog"""
import sys
from PySide6.QtWidgets import QDialog
import ui_configure


class ConfigureDialog(QDialog, ui_configure.Ui_Dialog):
    """Displays a configure dialog, inherits class generated from pyuic"""

    def __init__(self, parent=None):
        """Default constructor,  Parent window defaults to None"""
        super(ConfigureDialog, self).__init__(parent)

        # Set up the application
        self.setup()

    def setup(self):
        """Setup and start the application"""
        super(ConfigureDialog, self).setupUi(self)

        # Connect the OK button
        self.pushButtonOk.clicked.connect(self.okButtonClicked)

        # Connect the Cancel button
        self.pushButtonCancel.clicked.connect(self.cancelButtonClicked)

    def okButtonClicked(self):
        """Called when the OK button is clicked, emit a 'ConfigureDialogOk'
        signal along with a dictionary of the current dialog values e.g.
        { 'woeid': '248843',
            'pressure': 'in',
            'wind': 'mph',
            'temp': 'celcius',
            'distance': 'mi'}

        Close the window afterwards

        Signals:
        ConfigureDialogOk - Contains a dictionary of the current dialog values
        """
        values = {}
        values['woeid'] = str(self.lineEditWoeid.text())
        values['temperature'] = self.getTemperature()
        values['distance'] = self.getDistance()
        values['wind'] = self.getWind()
        values['pressure'] = self.getPressure()

        self.emit(SIGNAL('ConfigureDialogOk'), values)
        self.setVisible(False)

    def cancelButtonClicked(self):
        """Called when the cancel button is clicked"""
        self.setVisible(False)

    def setWoeid(self, woeid):
        """Set the dialog to display the Woeid

        Keyword arguments:
        woeid -- A woeid shown in the lineEdit, should be a 32bit integer

        Exceptions:
        ValueError -- Is raised if the woeid has an invalid value
        """
        # If cant cast woeid to int then must be invalid
        try:
            int(woeid)
        except ValueError as e:
            raise ValueError('Woeid is not a valid 32bit integer')

        # If woeid is greater than this then it is not a 32 unsigned integer
        if int(woeid) > 4294967295 or int(woeid) < 1:
            raise ValueError('Woeid is not a valid 32bit Integer')

        # Woeid should be valid, set the lineEdit
        self.lineEditWoeid.setText(str(woeid))

    def setTemperature(self, temperature):
        """Set the dialog to display a temp radio button

        Keyword arguments:
        temperature -- Set either the Fahrenheit or Celcius radio button, value
            should be either 'fahrenheit' or 'celcius'

        Exceptions:
        ValueError -- Is raised if the temperatire has an invalid value
        """
        # Check if value is valid
        if temperature not in ['fahrenheit', 'celcius']:
            raise ValueError('Invalid temp, use "fahrenheit" or "celcius"')

        # Woeid should be valid set the lineEdit
        if temperature == 'fahrenheit':
            self.radioButtonFahrenheit.setChecked(True)
        else:
            self.radioButtonCelcius.setChecked(True)

    def setDistance(self, distance):
        """Set the dialog to display a distance radio button

        Keyword arguments:
        distance -- Set either the Kilometers or Miles radio button value
            should be 'km' or 'mi'

        Exceptions:
        ValueError -- Is raised if the distance has an invalid value
        """
        # Check if value is valid
        if distance not in ['km', 'mi']:
            raise ValueError('Invalid distance, use "km" or "mi"')

        # distance should be valid set the correct radio button
        if distance == 'km':
            self.radioButtonKm.setChecked(True)
        else:
            self.radioButtonMi.setChecked(True)

    def setWind(self, wind):
        """Set the dialog to display the a wind radio button

        Keyword arguments:
        wind -- Set either the Kph or Mph radio button value
            should be 'kph' or 'mph'

        Exceptions:
        ValueError -- Is raised if the has an invalid value
        """
        # Check if value is valid
        if wind not in ['kph', 'mph']:
            raise ValueError('Invalid wind, use "kph" or "mph"')

        # distance should be valid set the correct radio button
        if wind == 'kph':
            self.radioButtonKph.setChecked(True)
        else:
            self.radioButtonMph.setChecked(True)

    def setPressure(self, pressure):
        """Set the dialog to display the a pressure radio button

        Keyword arguments:
        pressure -- Set either the Mb or In radio button value
            should be 'mb' or 'in'

        Exceptions:
        ValueError -- Is raised if the has an invalid value
        """
        # Check if value is valid
        if pressure not in ['mb', 'in']:
            raise ValueError('Invalid pressure, use "mb" or "in"')

        # distance should be valid set the correct radio button
        if pressure == 'mb':
            self.radioButtonMb.setChecked(True)
        else:
            self.radioButtonIn.setChecked(True)

    def getWoeid(self):
        """Return the woeid from the dialog

        Returns:
        A String containing the currently displayed Woeid
        """
        return str(self.lineEditWoeid.text())

    def getTemperature(self):
        """Return the temperature from the dialog

        Returns:
        A String containing either 'fahrenheit' or 'celcius'
        """
        if self.radioButtonFahrenheit.isChecked():
            return 'fahrenheit'
        else:
            return 'celcius'

    def getDistance(self):
        """Return the distance from the dialog

        Returns:
        A String containing either 'km' or 'mi'
        """
        if self.radioButtonKm.isChecked():
            return 'km'
        else:
            return 'mi'

    def getWind(self):
        """Return the wind from the dialog

        Returns:
        A String containing either 'kph' or 'mph'
        """
        if self.radioButtonKph.isChecked():
            return 'kph'
        else:
            return 'mph'

    def getPressure(self):
        """Return the wind from the dialog

        Returns:
        A String containing either 'mb' or 'in'
        """
        if self.radioButtonMb.isChecked():
            return 'mb'
        else:
            return 'in'

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = ConfigureDialog()
    main.show()
    app.exec_()
