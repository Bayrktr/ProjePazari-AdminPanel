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


def addUsersBackground(self):
    global recordButton, userName, userPassword, UserMail
    self.setFixedSize(300, 500)
    self.setWindowTitle("RegisterCompany")
    self.setStyleSheet("background-color: black")
    text = QLabel("User Name", self)
    text.setGeometry(80, 20, 150, 50)
    text.setStyleSheet("color: yellow;")
    text.setFont(QFont('Times', 15))
    userName = QLineEdit("UserName", self)
    userName.setGeometry(90, 70, 125, 50)
    userName.setStyleSheet("background-color: yellow")
    text = QLabel("User Password", self)
    text.setGeometry(70, 125, 175, 50)
    text.setStyleSheet("color: yellow;")
    text.setFont(QFont('Times', 15))
    userPassword = QLineEdit("UserPassword", self)
    userPassword.setGeometry(90, 180, 125, 50)
    userPassword.setStyleSheet("background-color: yellow")
    text = QLabel("User Mail", self)
    text.setGeometry(80, 240, 150, 50)
    text.setStyleSheet("color: yellow;")
    text.setFont(QFont('Times', 15))
    UserMail = QLineEdit("UserMail", self)
    UserMail.setGeometry(90, 300, 125, 50)
    UserMail.setStyleSheet("background-color: yellow")
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


def addUserRegisterButtonFunction():
    global recordButton
    return recordButton


def addUserNameText():
    global userName
    return userName.displayText()


def addUserPasswordText():
    global userPassword
    return userPassword.text()


def addUserMailText():
    global UserMail
    return UserMail.displayText()
