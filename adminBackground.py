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
from signUpFunction import *
from adminFunction import *

elemanList = ["name", "password", "mail", "code", "activity", "crdate"]


def adminBackground(self):
    global registerButton, refleshButton, deleteButton, comboBox, addCategoryToCompany, addfoodToCompany, deleteFoodsButton, deletecategorysButton, addProductButton, addUserButton
    companyList = companyNameList()
    companyList.remove("admin")
    self.setWindowTitle("Admin")
    self.setFixedSize(1100, 600)
    self.setStyleSheet("background-color: lightblue")
    registerButton = QPushButton("Register Company", self)
    registerButton.setGeometry(240, 20, 140, 60)
    registerButton.setStyleSheet("QPushButton"
                                 "{"
                                 "background-color : lightgreen;"
                                 "}"
                                 )
    refleshButton = QPushButton("RH", self)
    refleshButton.setGeometry(180, 20, 40, 40)
    refleshButton.setStyleSheet("QPushButton"
                                "{"
                                "background-color : lightgreen;"
                                "}"
                                )

    deleteButton = QPushButton("Delete", self)
    deleteButton.setGeometry(200, 520, 100, 60)
    deleteButton.setStyleSheet("QPushButton"
                               "{"
                               "background-color : lightgreen;"
                               "}"
                               )
    addfoodToCompany = QPushButton("Add Food", self)
    addfoodToCompany.setGeometry(200, 440, 100, 60)
    addfoodToCompany.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightgreen;"
                                   "}"
                                   )
    addCategoryToCompany = QPushButton("Add Category", self)
    addCategoryToCompany.setGeometry(200, 360, 100, 60)
    addCategoryToCompany.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color : lightgreen;"
                                       "}"
                                       )
    comboBox = QComboBox(self)
    comboBox.setGeometry(20, 20, 150, 100)
    comboBox.setStyleSheet("background-color: green")
    comboBox.setStyleSheet("font-size: 12pt")
    comboBox.addItems(companyList)

    deleteFoodsButton = QPushButton("Delete Food", self)
    deleteFoodsButton.setGeometry(200, 280, 100, 60)
    deleteFoodsButton.setStyleSheet("QPushButton"
                                    "{"
                                    "background-color : lightgreen;"
                                    "}"
                                    )
    deletecategorysButton = QPushButton("Delete Category", self)
    deletecategorysButton.setGeometry(200, 200, 100, 60)
    deletecategorysButton.setStyleSheet("QPushButton"
                                        "{"
                                        "background-color : lightgreen;"
                                        "}")
    addProductButton = QPushButton("Add Product", self)
    addProductButton.setGeometry(200, 120, 100, 60)
    addProductButton.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightgreen;"
                                   "}")
    addUserButton = QPushButton("Add User", self)
    addUserButton.setGeometry(20, 520, 100, 60)
    addUserButton.setStyleSheet("QPushButton"
                                "{"
                                "background-color : lightgreen;"
                                "}")


def data(self):
    startX = 300
    comboBoxName = comboBoxFunction().currentText()
    print(comboBoxName)
    for x in elemanList:
        startX += 110
        startY = 20
        liste = takeData(x)
        for y in liste:
            pressData(self, y, startX, startY)
            startY += 12


def pressData(self, y, startX, startY):
    label = QLabel(f"{y}", self)
    label.setGeometry(startX, startY, 110, 12)
    label.setStyleSheet("background-color: lightgreen")


def registerButtonFunction():
    global registerButton
    return registerButton


def refleshButtonFunction():
    global refleshButton
    return refleshButton


def deleteButtonFunction():
    global deleteButton
    return deleteButton


def comboBoxFunction():
    global comboBox
    return comboBox


def addCategoryButtonFunction():
    global addCategoryToCompany
    return addCategoryToCompany


def addFoodButtonFunction():
    global addfoodToCompany
    return addfoodToCompany


def deleteFoodsButtonFunction():
    global deleteFoodsButton
    return deleteFoodsButton


def deleteCategoryFunction():
    global deletecategorysButton
    return deletecategorysButton


def addProductFunction():
    global addProductButton
    return addProductButton


def addUserButtonFunction():
    global addUserButton
    return addUserButton
