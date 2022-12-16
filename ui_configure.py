# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configure.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(354, 349)
        self.groupBoxDistance = QGroupBox(Dialog)
        self.groupBoxDistance.setObjectName(u"groupBoxDistance")
        self.groupBoxDistance.setGeometry(QRect(10, 130, 331, 51))
        self.radioButtonKm = QRadioButton(self.groupBoxDistance)
        self.radioButtonKm.setObjectName(u"radioButtonKm")
        self.radioButtonKm.setGeometry(QRect(150, 20, 91, 23))
        self.radioButtonMi = QRadioButton(self.groupBoxDistance)
        self.radioButtonMi.setObjectName(u"radioButtonMi")
        self.radioButtonMi.setGeometry(QRect(250, 20, 83, 23))
        self.radioButtonMi.setChecked(True)
        self.labelDistance = QLabel(self.groupBoxDistance)
        self.labelDistance.setObjectName(u"labelDistance")
        self.labelDistance.setGeometry(QRect(10, 20, 111, 20))
        self.groupBoxTemperature = QGroupBox(Dialog)
        self.groupBoxTemperature.setObjectName(u"groupBoxTemperature")
        self.groupBoxTemperature.setGeometry(QRect(10, 70, 331, 51))
        self.radioButtonFahrenheit = QRadioButton(self.groupBoxTemperature)
        self.radioButtonFahrenheit.setObjectName(u"radioButtonFahrenheit")
        self.radioButtonFahrenheit.setGeometry(QRect(151, 16, 91, 23))
        self.labelTemperature = QLabel(self.groupBoxTemperature)
        self.labelTemperature.setObjectName(u"labelTemperature")
        self.labelTemperature.setGeometry(QRect(10, 18, 131, 20))
        self.radioButtonCelcius = QRadioButton(self.groupBoxTemperature)
        self.radioButtonCelcius.setObjectName(u"radioButtonCelcius")
        self.radioButtonCelcius.setGeometry(QRect(247, 17, 83, 23))
        self.radioButtonCelcius.setChecked(True)
        self.groupWoeid = QGroupBox(Dialog)
        self.groupWoeid.setObjectName(u"groupWoeid")
        self.groupWoeid.setGeometry(QRect(10, 10, 331, 51))
        self.lineEditWoeid = QLineEdit(self.groupWoeid)
        self.lineEditWoeid.setObjectName(u"lineEditWoeid")
        self.lineEditWoeid.setGeometry(QRect(132, 14, 113, 23))
        self.lineEditWoeid.setMaxLength(8)
        self.labelId = QLabel(self.groupWoeid)
        self.labelId.setObjectName(u"labelId")
        self.labelId.setGeometry(QRect(10, 20, 101, 17))
        self.pushButtonOk = QPushButton(Dialog)
        self.pushButtonOk.setObjectName(u"pushButtonOk")
        self.pushButtonOk.setGeometry(QRect(110, 310, 113, 32))
        self.pushButtonCancel = QPushButton(Dialog)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        self.pushButtonCancel.setGeometry(QRect(230, 310, 113, 32))
        self.groupWind = QGroupBox(Dialog)
        self.groupWind.setObjectName(u"groupWind")
        self.groupWind.setGeometry(QRect(10, 190, 331, 51))
        self.radioButtonKph = QRadioButton(self.groupWind)
        self.radioButtonKph.setObjectName(u"radioButtonKph")
        self.radioButtonKph.setGeometry(QRect(150, 16, 83, 23))
        self.labelWind = QLabel(self.groupWind)
        self.labelWind.setObjectName(u"labelWind")
        self.labelWind.setGeometry(QRect(10, 20, 131, 20))
        self.radioButtonMph = QRadioButton(self.groupWind)
        self.radioButtonMph.setObjectName(u"radioButtonMph")
        self.radioButtonMph.setGeometry(QRect(247, 17, 83, 23))
        self.radioButtonMph.setChecked(True)
        self.groupBoxPressure = QGroupBox(Dialog)
        self.groupBoxPressure.setObjectName(u"groupBoxPressure")
        self.groupBoxPressure.setGeometry(QRect(10, 250, 331, 51))
        self.radioButtonIn = QRadioButton(self.groupBoxPressure)
        self.radioButtonIn.setObjectName(u"radioButtonIn")
        self.radioButtonIn.setGeometry(QRect(250, 20, 83, 23))
        self.labelPressure = QLabel(self.groupBoxPressure)
        self.labelPressure.setObjectName(u"labelPressure")
        self.labelPressure.setGeometry(QRect(10, 20, 111, 20))
        self.radioButtonMb = QRadioButton(self.groupBoxPressure)
        self.radioButtonMb.setObjectName(u"radioButtonMb")
        self.radioButtonMb.setGeometry(QRect(150, 20, 83, 23))
        self.radioButtonMb.setChecked(True)
        QWidget.setTabOrder(self.lineEditWoeid, self.radioButtonFahrenheit)
        QWidget.setTabOrder(self.radioButtonFahrenheit, self.radioButtonCelcius)
        QWidget.setTabOrder(self.radioButtonCelcius, self.radioButtonKm)
        QWidget.setTabOrder(self.radioButtonKm, self.radioButtonMi)
        QWidget.setTabOrder(self.radioButtonMi, self.radioButtonKph)
        QWidget.setTabOrder(self.radioButtonKph, self.radioButtonMph)
        QWidget.setTabOrder(self.radioButtonMph, self.radioButtonMb)
        QWidget.setTabOrder(self.radioButtonMb, self.radioButtonIn)
        QWidget.setTabOrder(self.radioButtonIn, self.pushButtonOk)
        QWidget.setTabOrder(self.pushButtonOk, self.pushButtonCancel)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configure", None))
        self.groupBoxDistance.setTitle("")
        self.radioButtonKm.setText(QCoreApplication.translate("Dialog", u"&Kilometers", None))
        self.radioButtonMi.setText(QCoreApplication.translate("Dialog", u"&Miles", None))
        self.labelDistance.setText(QCoreApplication.translate("Dialog", u"Show Distance in", None))
        self.groupBoxTemperature.setTitle("")
        self.radioButtonFahrenheit.setText(QCoreApplication.translate("Dialog", u"&Fahrenheit", None))
        self.labelTemperature.setText(QCoreApplication.translate("Dialog", u"Show Temperature in", None))
        self.radioButtonCelcius.setText(QCoreApplication.translate("Dialog", u"C&elcius", None))
        self.groupWoeid.setTitle("")
#if QT_CONFIG(tooltip)
        self.labelId.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.labelId.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.labelId.setText(QCoreApplication.translate("Dialog", u"Woeid ", None))
        self.pushButtonOk.setText(QCoreApplication.translate("Dialog", u"&OK", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Dialog", u"&Cancel", None))
        self.groupWind.setTitle("")
        self.radioButtonKph.setText(QCoreApplication.translate("Dialog", u"K&ph", None))
        self.labelWind.setText(QCoreApplication.translate("Dialog", u"Show Wind Speed in", None))
        self.radioButtonMph.setText(QCoreApplication.translate("Dialog", u"Mp&h", None))
        self.groupBoxPressure.setTitle("")
        self.radioButtonIn.setText(QCoreApplication.translate("Dialog", u"&In", None))
        self.labelPressure.setText(QCoreApplication.translate("Dialog", u"Show Pressure in", None))
        self.radioButtonMb.setText(QCoreApplication.translate("Dialog", u"M&b", None))
    # retranslateUi

