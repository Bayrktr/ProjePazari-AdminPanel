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
from addCategoryFunction import *
from addFoodFunction import *

elemanList = ["name", "price", "category", "code", "number", "crdate"]


def addFoodsBackground(self, companyNameComboBox):
    global categoryComboBox, foodName, foodPrice, recordFood
    self.setFixedSize(400, 700)
    self.setStyleSheet("background-color: lightblue")
    foodName = QLineEdit("FoodName", self)
    foodName.setGeometry(125, 20, 140, 50)
    foodName.setStyleSheet("background-color: lightgreen")
    foodPrice = QLineEdit("FoodPrice", self)
    foodPrice.setGeometry(125, 80, 140, 50)
    foodPrice.setStyleSheet("background-color: lightgreen")
    categoryComboBox = QComboBox(self)
    categoryComboBox.setGeometry(125, 140, 150, 60)
    categoryComboBox.setStyleSheet("background-color: green")
    categoryComboBox.setStyleSheet("font-size: 12pt")
    categoryComboBox.addItems(takeCategoryNames(companyNameComboBox))
    recordFood = QPushButton("Record", self)
    recordFood.setGeometry(125, 210, 140, 50)
    recordFood.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightgreen;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : red;"
                             "}"
                             )


def mainDataFood(self, companyNameComboBox):
    startX = -80
    for x in elemanList:
        startX += 80
        startY = 280
        liste = takeDataFood(x, companyNameComboBox)
        for y in liste:
            pressData(self, y, startX, startY)
            startY += 12


def pressData(self, y, startX, startY):
    label = QLabel(f"{y}", self)
    label.setGeometry(startX, startY, 80, 12)
    label.setStyleSheet("background-color: lightgreen")


def selectCategoryComboBoxFunc():
    global categoryComboBox
    return categoryComboBox

def recordFoodButton():
    global recordFood
    return recordFood

def foodNameText():
    global foodName
    return foodName

def foodPriceText():
    global foodPrice
    return foodPrice
