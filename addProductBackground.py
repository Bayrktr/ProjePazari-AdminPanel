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
from addFoodFunction import *


def addProductsBackground(self, foodName, foodNumber):
    global selectFoodNameComboBox, addButton, reduceButton, addProductNumberText
    self.setFixedSize(300, 500)
    self.setStyleSheet("background-color: lightblue")
    selectFoodNameComboBox = QComboBox(self)
    selectFoodNameComboBox.setGeometry(60, 40, 200, 60)
    selectFoodNameComboBox.setStyleSheet("font-size: 12pt")
    selectFoodNameComboBox.addItems(foodName)
    showTheNumber = QLabel(f"Number:{foodNumber}", self)
    showTheNumber.setGeometry(10, 10, 120, 15)
    showTheNumber.setStyleSheet("background-color: lightgreen")
    showTheNumber.setStyleSheet("font-size:12pt")

    addProductNumberText = QLineEdit("0", self)
    addProductNumberText.setGeometry(80, 120, 150, 60)
    addProductNumberText.setStyleSheet("background-color: lightgreen")
    addButton = QPushButton("Add", self)
    addButton.setGeometry(30, 200, 110, 50)
    addButton.setStyleSheet("background-color: lightgreen")
    reduceButton = QPushButton("Reduce", self)
    reduceButton.setGeometry(150, 200, 110, 50)
    reduceButton.setStyleSheet("background-color: lightgreen")


def selectFoodProductFunction():
    global selectFoodNameComboBox
    return selectFoodNameComboBox


def addProductButtonFunction():
    global addButton
    return addButton


def reduceProductFunction():
    global reduceButton
    return reduceButton


def addProductTextFunction():
    global addProductNumberText
    return addProductNumberText.text()
