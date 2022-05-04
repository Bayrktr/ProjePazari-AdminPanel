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
from menuSelectFunction import *


def selectMenuBackground(self, companyNameComboBox):
    global selectMenuNameComboBox, deleteMenuButton, selectMenuButton
    self.setFixedSize(300, 450)
    self.setStyleSheet("background-color: lightblue")
    selectMenuNameComboBox = QComboBox(self)
    selectMenuNameComboBox.setGeometry(60, 40, 200, 60)
    selectMenuNameComboBox.setStyleSheet("background-color: green")
    selectMenuNameComboBox.setStyleSheet("font-size: 15pt")
    selectMenuNameComboBox.addItems(allMenuNames(companyNameComboBox))
    deleteMenuButton = QPushButton("Delete", self)
    deleteMenuButton.setGeometry(70, 120, 180, 60)
    deleteMenuButton.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightgreen;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : red;"
                                   "}")
    selectMenuButton = QPushButton("Select", self)
    selectMenuButton.setGeometry(70, 210, 180, 60)
    selectMenuButton.setStyleSheet("QPushButton"
                                   "{"
                                   "background-color : lightgreen;"
                                   "}"
                                   "QPushButton::pressed"
                                   "{"
                                   "background-color : red;"
                                   "}")


def selectMenuNameComboBoxFunction():
    global selectMenuNameComboBox
    return selectMenuNameComboBox


def deleteMenuButtonFunction():
    global deleteMenuButton
    return deleteMenuButton


def selectMenuButtonFunction():
    global selectMenuButton
    return selectMenuButton
