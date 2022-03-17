import random
import re
import socket
import string
import sys
from datetime import datetime

import mysql.connector
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QComboBox


def registerBackground(self):
    global recordButton, companyName, companyPassword, companyMail
    self.setFixedSize(300, 500)
    self.setWindowTitle("RegisterCompany")
    self.setStyleSheet("background-color: black")
    text = QLabel("Company Name", self)
    text.setGeometry(80, 20, 150, 50)
    text.setStyleSheet("color: yellow;")
    text.setFont(QFont('Times', 15))
    companyName = QLineEdit("CompanyName", self)
    companyName.setGeometry(90, 70, 125, 50)
    companyName.setStyleSheet("background-color: yellow")
    text = QLabel("Company Password", self)
    text.setGeometry(70, 125, 175, 50)
    text.setStyleSheet("color: yellow;")
    text.setFont(QFont('Times', 15))
    companyPassword = QLineEdit("CompanyPassword", self)
    companyPassword.setGeometry(90, 180, 125, 50)
    companyPassword.setStyleSheet("background-color: yellow")
    text = QLabel("Company Mail", self)
    text.setGeometry(80, 240, 150, 50)
    text.setStyleSheet("color: yellow;")
    text.setFont(QFont('Times', 15))
    companyMail = QLineEdit("CompanyMail", self)
    companyMail.setGeometry(90, 300, 125, 50)
    companyMail.setStyleSheet("background-color: yellow")
    recordButton = QPushButton("Record", self)
    recordButton.setGeometry(80, 380, 145, 50)
    recordButton.setStyleSheet("QPushButton"
                               "{"
                               "background-color : yellow;"
                               "}"
                               "QPushButton::pressed"
                               "{"
                               "background-color : red;"
                               "}"
                               )


def registerButton():
    global recordButton
    return recordButton


def companyNameText():
    global companyName
    return companyName.displayText()


def companyPasswordText():
    global companyPassword
    return companyPassword.displayText()


def companyMailText():
    global companyMail
    return companyMail.displayText()
