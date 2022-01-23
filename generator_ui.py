# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generatorVsAaYY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(308, 252)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")

        self.horizontalLayout.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.labelResultado = QLabel(self.centralwidget)
        self.labelResultado.setObjectName(u"labelResultado")
        font1 = QFont()
        font1.setPointSize(24)
        self.labelResultado.setFont(font1)

        self.verticalLayout.addWidget(self.labelResultado)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cleanFieldsButton = QPushButton(self.centralwidget)
        self.cleanFieldsButton.setObjectName(u"cleanFieldsButton")

        self.horizontalLayout_2.addWidget(self.cleanFieldsButton)

        self.generateResultButton = QPushButton(self.centralwidget)
        self.generateResultButton.setObjectName(u"generateResultButton")

        self.horizontalLayout_2.addWidget(self.generateResultButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rango desde 0: ", None))
        self.labelResultado.setText(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.cleanFieldsButton.setText(QCoreApplication.translate("MainWindow", u"Reiniciar valores", None))
        self.generateResultButton.setText(QCoreApplication.translate("MainWindow", u"Generar resultado", None))
    # retranslateUi

