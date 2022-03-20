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


def deleteUsersBackground(self, newUserPassword, newUserMail, userList):
    global deleteUserButton, usersComboBox, updateUserButton, newUserPasswordLine, newUserMailLine
    self.setFixedSize(600, 400)
    self.setStyleSheet("background-color: lightblue")
    usersComboBox = QComboBox(self)
    usersComboBox.setGeometry(50, 20, 500, 60)
    usersComboBox.setStyleSheet("background-color: green")
    usersComboBox.setStyleSheet("font-size: 11pt")
    usersComboBox.addItems(userList)
    deleteUserButton = QPushButton("Delete", self)
    deleteUserButton.setGeometry(280, 260, 140, 50)
    deleteUserButton.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightgreen;"
                                   "}"
                                   )
    updateUserButton = QPushButton("Update", self)
    updateUserButton.setGeometry(120, 260, 140, 50)
    updateUserButton.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightgreen;"
                                   "}"
                                   )
    newUserPasswordLine = QLineEdit(f"{newUserPassword}", self)
    newUserPasswordLine.setGeometry(210, 100, 150, 60)
    newUserPasswordLine.setStyleSheet("background-color:lightgreen")
    newUserMailLine = QLineEdit(f"{newUserMail}", self)
    newUserMailLine.setGeometry(210, 180, 150, 60)
    newUserMailLine.setStyleSheet("background-color:lightgreen")


def creatingList(companyNameComboBox):
    liste = []
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = "SELECT * FROM userrecords"
    cursor.execute(sql)
    for x in cursor.fetchall():
        kelime = ""
        for y in x:
            kelime += (str(y) + 3 * " ")
        liste.append(kelime)
    return liste


def deleteUserButtonFunction():
    global deleteUserButton
    return deleteUserButton


def usersComboBoxFunction():
    global usersComboBox
    return usersComboBox


def updateUserButtonFunction():
    global updateUserButton
    return updateUserButton


def newUserPasswordLineText():
    global newUserPasswordLine
    return newUserPasswordLine.displayText()


def newUserMailLineText():
    global newUserMailLine
    return newUserMailLine.displayText()
