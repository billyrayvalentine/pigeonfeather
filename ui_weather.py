# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weather.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QSizePolicy, QWidget)

class Ui_Weather(object):
    def setupUi(self, Weather):
        if not Weather.objectName():
            Weather.setObjectName(u"Weather")
        Weather.resize(394, 230)
        self.frame = QFrame(Weather)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 64, 64))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.labelIcon = QLabel(self.frame)
        self.labelIcon.setObjectName(u"labelIcon")
        self.labelIcon.setGeometry(QRect(0, 0, 64, 64))
        self.labelFSunset = QLabel(Weather)
        self.labelFSunset.setObjectName(u"labelFSunset")
        self.labelFSunset.setGeometry(QRect(20, 80, 56, 18))
        self.labelSunset = QLabel(Weather)
        self.labelSunset.setObjectName(u"labelSunset")
        self.labelSunset.setGeometry(QRect(130, 80, 61, 18))
        self.labelFSunrise = QLabel(Weather)
        self.labelFSunrise.setObjectName(u"labelFSunrise")
        self.labelFSunrise.setGeometry(QRect(20, 110, 56, 18))
        self.labelSunrise = QLabel(Weather)
        self.labelSunrise.setObjectName(u"labelSunrise")
        self.labelSunrise.setGeometry(QRect(130, 110, 61, 18))
        self.labelTemp = QLabel(Weather)
        self.labelTemp.setObjectName(u"labelTemp")
        self.labelTemp.setGeometry(QRect(100, 20, 281, 36))
        font = QFont()
        font.setPointSize(16)
        self.labelTemp.setFont(font)
        self.labelFWindChill = QLabel(Weather)
        self.labelFWindChill.setObjectName(u"labelFWindChill")
        self.labelFWindChill.setGeometry(QRect(20, 140, 71, 18))
        self.labelWindChill = QLabel(Weather)
        self.labelWindChill.setObjectName(u"labelWindChill")
        self.labelWindChill.setGeometry(QRect(130, 140, 61, 18))
        self.labelFWindSpeed = QLabel(Weather)
        self.labelFWindSpeed.setObjectName(u"labelFWindSpeed")
        self.labelFWindSpeed.setGeometry(QRect(20, 170, 81, 18))
        self.labelWindSpeed = QLabel(Weather)
        self.labelWindSpeed.setObjectName(u"labelWindSpeed")
        self.labelWindSpeed.setGeometry(QRect(130, 170, 61, 18))
        self.labelFWindDirection = QLabel(Weather)
        self.labelFWindDirection.setObjectName(u"labelFWindDirection")
        self.labelFWindDirection.setGeometry(QRect(20, 200, 101, 18))
        self.labelWindDirection = QLabel(Weather)
        self.labelWindDirection.setObjectName(u"labelWindDirection")
        self.labelWindDirection.setGeometry(QRect(130, 200, 61, 18))
        self.labelFPressure = QLabel(Weather)
        self.labelFPressure.setObjectName(u"labelFPressure")
        self.labelFPressure.setGeometry(QRect(210, 140, 71, 18))
        self.labelFHumidity = QLabel(Weather)
        self.labelFHumidity.setObjectName(u"labelFHumidity")
        self.labelFHumidity.setGeometry(QRect(210, 80, 61, 18))
        self.labelVisibility = QLabel(Weather)
        self.labelVisibility.setObjectName(u"labelVisibility")
        self.labelVisibility.setGeometry(QRect(290, 110, 61, 21))
        self.labelPressure = QLabel(Weather)
        self.labelPressure.setObjectName(u"labelPressure")
        self.labelPressure.setGeometry(QRect(290, 140, 81, 18))
        self.labelFVisibility = QLabel(Weather)
        self.labelFVisibility.setObjectName(u"labelFVisibility")
        self.labelFVisibility.setGeometry(QRect(210, 110, 56, 18))
        self.labelHumidity = QLabel(Weather)
        self.labelHumidity.setObjectName(u"labelHumidity")
        self.labelHumidity.setGeometry(QRect(290, 80, 61, 16))
        self.labelRising = QLabel(Weather)
        self.labelRising.setObjectName(u"labelRising")
        self.labelRising.setGeometry(QRect(290, 170, 61, 18))
        self.labelFRising = QLabel(Weather)
        self.labelFRising.setObjectName(u"labelFRising")
        self.labelFRising.setGeometry(QRect(210, 170, 71, 18))
        self.labelFLastUpdate = QLabel(Weather)
        self.labelFLastUpdate.setObjectName(u"labelFLastUpdate")
        self.labelFLastUpdate.setGeometry(QRect(298, 213, 56, 20))
        font1 = QFont()
        font1.setPointSize(7)
        self.labelFLastUpdate.setFont(font1)
        self.labelLastUpdate = QLabel(Weather)
        self.labelLastUpdate.setObjectName(u"labelLastUpdate")
        self.labelLastUpdate.setGeometry(QRect(353, 213, 41, 20))
        self.labelLastUpdate.setFont(font1)

        self.retranslateUi(Weather)

        QMetaObject.connectSlotsByName(Weather)
    # setupUi

    def retranslateUi(self, Weather):
        Weather.setWindowTitle(QCoreApplication.translate("Weather", u"Dialog", None))
        self.labelIcon.setText("")
        self.labelFSunset.setText(QCoreApplication.translate("Weather", u"Sunset", None))
        self.labelSunset.setText(QCoreApplication.translate("Weather", u"Unknown", None))
        self.labelFSunrise.setText(QCoreApplication.translate("Weather", u"Sunrise", None))
        self.labelSunrise.setText(QCoreApplication.translate("Weather", u"Unknown", None))
        self.labelTemp.setText(QCoreApplication.translate("Weather", u"22 c Scattered Thunderstorms", None))
        self.labelFWindChill.setText(QCoreApplication.translate("Weather", u"Feels like ", None))
        self.labelWindChill.setText(QCoreApplication.translate("Weather", u"Unknown", None))
        self.labelFWindSpeed.setText(QCoreApplication.translate("Weather", u"Wind Speed", None))
        self.labelWindSpeed.setText(QCoreApplication.translate("Weather", u"Unknown", None))
        self.labelFWindDirection.setText(QCoreApplication.translate("Weather", u"Wind Direction", None))
        self.labelWindDirection.setText(QCoreApplication.translate("Weather", u"Unknown", None))
        self.labelFPressure.setText(QCoreApplication.translate("Weather", u"Pressure", None))
        self.labelFHumidity.setText(QCoreApplication.translate("Weather", u"Humidity", None))
        self.labelVisibility.setText(QCoreApplication.translate("Weather", u"Unknown", None))
        self.labelPressure.setText(QCoreApplication.translate("Weather", u"Unknown", None))
        self.labelFVisibility.setText(QCoreApplication.translate("Weather", u"Visibility", None))
        self.labelHumidity.setText(QCoreApplication.translate("Weather", u"Unknown", None))
        self.labelRising.setText(QCoreApplication.translate("Weather", u"Unknown", None))
        self.labelFRising.setText(QCoreApplication.translate("Weather", u"Tendancy", None))
        self.labelFLastUpdate.setText(QCoreApplication.translate("Weather", u"last update:", None))
        self.labelLastUpdate.setText(QCoreApplication.translate("Weather", u"00:00:00", None))
    # retranslateUi

