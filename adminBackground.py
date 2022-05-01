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
butonColor = "orange"


def adminBackground(self):
    global registerButton, refleshButton, deleteButton, comboBox, addCategoryToCompany, addfoodToCompany, deleteFoodsButton, deletecategorysButton, addProductButton, addUserButton, deleteUserButton, menuOptionsButton
    companyList = companyNameList()
    companyList.remove("admin")
    self.setWindowTitle("Admin")
    self.setFixedSize(1100, 600)
    self.setStyleSheet("background-color: gray")
    registerButton = QPushButton("Register Company", self)
    registerButton.setGeometry(10, 10, 100, 40)
    registerButton.setStyleSheet("QPushButton"
                                 "{"
                                 f"background-color : {butonColor};"
                                 "}"
                                 )
    refleshButton = QPushButton("RH", self)
    refleshButton.setGeometry(10, 600, 40, 40)
    refleshButton.setStyleSheet("QPushButton"
                                "{"
                                f"background-color : {butonColor};"
                                "}"
                                )

    deleteButton = QPushButton("Delete", self)
    deleteButton.setGeometry(10, 60, 100, 40)
    deleteButton.setStyleSheet("QPushButton"
                               "{"
                               f"background-color : {butonColor};"
                               "}"
                               )
    addfoodToCompany = QPushButton("Add Food", self)
    addfoodToCompany.setGeometry(10, 110, 100, 40)
    addfoodToCompany.setStyleSheet("QPushButton"
                                   "{"
                                   f"background-color : {butonColor};"
                                   "}"
                                   )
    addCategoryToCompany = QPushButton("Add Category", self)
    addCategoryToCompany.setGeometry(10, 160, 100, 40)
    addCategoryToCompany.setStyleSheet("QPushButton"
                                       "{"
                                       f"background-color : {butonColor};"
                                       "}"
                                       )
    comboBox = QComboBox(self)
    comboBox.setGeometry(140, 10, 120, 60)
    comboBox.setStyleSheet("background-color: orange")
    comboBox.setStyleSheet("font-size: 12pt")
    comboBox.addItems(companyList)

    deleteFoodsButton = QPushButton("Delete Food", self)
    deleteFoodsButton.setGeometry(10, 210, 100, 40)
    deleteFoodsButton.setStyleSheet("QPushButton"
                                    "{"
                                    f"background-color : {butonColor};"
                                    "}"
                                    )
    deletecategorysButton = QPushButton("Delete Category", self)
    deletecategorysButton.setGeometry(10, 260, 100, 40)
    deletecategorysButton.setStyleSheet("QPushButton"
                                        "{"
                                        f"background-color : {butonColor};"
                                        "}")
    addProductButton = QPushButton("Add Product", self)
    addProductButton.setGeometry(10, 310, 100, 40)
    addProductButton.setStyleSheet("QPushButton"
                                   "{"
                                   f"background-color : {butonColor};"
                                   "}")
    addUserButton = QPushButton("Add User", self)
    addUserButton.setGeometry(10, 360, 100, 40)
    addUserButton.setStyleSheet("QPushButton"
                                "{"
                                f"background-color : {butonColor};"
                                "}")
    deleteUserButton = QPushButton("Delete User", self)
    deleteUserButton.setGeometry(10, 410, 100, 40)
    deleteUserButton.setStyleSheet("QPushButton"
                                   "{"
                                   f"background-color : {butonColor};"
                                   "}")
    menuOptionsButton = QPushButton("MenuOptions", self)
    menuOptionsButton.setGeometry(10, 460, 100, 40)
    menuOptionsButton.setStyleSheet("QPushButton"
                                    "{"
                                    f"background-color : {butonColor};"
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
    label.setStyleSheet("background-color: orange")


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


def deleteUserFunction():
    global deleteUserButton
    return deleteUserButton


def menuOptionsFunction():
    global menuOptionsButton
    return menuOptionsButton
