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


def deleteFoodsBackground(self, companyNameComboBox, foodNameCat, foodPrice, foodName):
    global foodListComboBox, updateFoodButton, deleteFoodButton, newprice, categorysComboBox
    self.setFixedSize(300, 600)
    self.setStyleSheet("background-color: lightblue")
    foodListComboBox = QComboBox(self)
    foodListComboBox.setGeometry(50, 20, 200, 60)
    foodListComboBox.setStyleSheet("background-color: green")
    foodListComboBox.setStyleSheet("font-size: 12pt")
    foodListComboBox.addItems(foodName)
    categorysComboBox = QComboBox(self)
    categorysComboBox.setGeometry(50, 100, 200, 60)
    categorysComboBox.setStyleSheet("background-color: green")
    categorysComboBox.setStyleSheet("font-size: 12pt")
    categorysComboBox.addItems(foodNameCat)
    newprice = QLineEdit(f"{foodPrice}", self)
    newprice.setGeometry(75, 180, 140, 50)
    newprice.setStyleSheet("background-color: lightgreen")
    updateFoodButton = QPushButton("Update", self)
    updateFoodButton.setGeometry(75, 240, 140, 50)
    updateFoodButton.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightblue;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : red;"
                                   "}"
                                   )
    updateFoodButton.setFont(QFont('Times font', 15))
    deleteFoodButton = QPushButton("Delete", self)
    deleteFoodButton.setGeometry(75, 300, 140, 50)
    deleteFoodButton.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightblue;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : red;"
                                   "}"
                                   )
    deleteFoodButton.setFont(QFont('Times font', 15))


def foodListComboBoxFunction():
    global foodListComboBox
    return foodListComboBox


def updateFoodFunction():
    global updateFoodButton
    return updateFoodButton


def deleteFoodFunction():
    global deleteFoodButton
    return deleteFoodButton


def newPriceFunction():
    global newprice
    return newprice


def foodCategoryFunction():
    global categorysComboBox
    return categorysComboBox
