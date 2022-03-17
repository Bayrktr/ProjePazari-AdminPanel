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


def signInBackground(self):
    global button, username, password
    self.setFixedSize(300, 500)
    self.setStyleSheet("background-color:black")
    self.setWindowTitle('SignIn')

    username = QLineEdit("", self)
    username.setGeometry(75, 75, 150, 50)

    username.setStyleSheet("QLineEdit"
                           "{"
                           "background-color : yellow;"
                           "}"
                           )

    password = QLineEdit(self)
    password.setGeometry(75, 150, 150, 50)
    password.setEchoMode(QLineEdit.Password)
    password.setStyleSheet("QLineEdit"
                           "{"
                           "background-color : yellow;"
                           "}")

    button = QPushButton("SingIn", self)
    button.setGeometry(75, 225, 150, 50)
    button.setStyleSheet("QPushButton"
                         "{"
                         "background-color : yellow;"
                         "}"
                         "QPushButton::pressed"
                         "{"
                         "background-color : red;"
                         "}"
                         )
    button.setFont(QFont('Times font', 15))


def usernameFunction():
    global username
    return username.displayText()


def passwordFunction():
    global password
    return password.text()


def buttonFunction():
    global button
    return button
