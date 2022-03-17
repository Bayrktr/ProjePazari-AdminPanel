import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from adminBackground import *
from adminFunction import *
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QComboBox
from addCategoryFunction import *


def addCategoryBackground(self):
    global categoryName, record
    self.setFixedSize(300, 600)
    self.setStyleSheet("background-color: lightblue")
    categoryName = QLineEdit("CategoryName", self)
    categoryName.setGeometry(75, 20, 140, 50)
    categoryName.setStyleSheet("background-color: lightgreen")
    record = QPushButton("Record", self)
    record.setGeometry(75, 80, 140, 40)
    record.setStyleSheet("QPushButton"
                         "{"
                         "background-color : lightgreen;"
                         "}"
                         "QPushButton::pressed"
                         "{"
                         "background-color : red;"
                         "}"
                         )


def categoryNameFunction():
    global categoryName
    return categoryName.displayText()


def addCategoryRecordFunction():
    global record
    return record


def mainData(self, companyNameComboBox):
    startY = 120
    print(companyNameComboBox)
    for x in takeCategoryNames(companyNameComboBox):
        startX = 0
        startY += 15
        liste = takaData(x, companyNameComboBox)
        for y in liste:
            pressData(self, y, startX, startY)
            startX += 110


def pressData(self, y, startX, startY):
    label = QLabel(f"{y}", self)
    label.setGeometry(startX, startY, 110, 15)
    label.setStyleSheet("background-color: lightgreen")
