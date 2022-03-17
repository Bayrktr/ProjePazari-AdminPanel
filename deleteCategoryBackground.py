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


def deleteCategorysBackground(self, companyNameComboBox):
    global selectDelCategoryComboBox, deleteCategoryButton
    self.setFixedSize(300, 450)
    self.setStyleSheet("background-color: lightblue")
    selectDelCategoryComboBox = QComboBox(self)
    selectDelCategoryComboBox.setGeometry(60, 40, 200, 60)
    selectDelCategoryComboBox.setStyleSheet("background-color: green")
    selectDelCategoryComboBox.setStyleSheet("font-size: 15pt")
    selectDelCategoryComboBox.addItems(takeCategoryNames(companyNameComboBox))
    deleteCategoryButton = QPushButton("Delete", self)
    deleteCategoryButton.setGeometry(70, 120, 180, 60)
    deleteCategoryButton.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color : lightgreen;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : red;"
                                       "}")


def selectDelCategoryFunction():
    global selectDelCategoryComboBox
    return selectDelCategoryComboBox


def deleteCategoryButtonFunction():
    global deleteCategoryButton
    return deleteCategoryButton
