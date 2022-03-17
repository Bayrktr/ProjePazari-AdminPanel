import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector

from addCategoryFunction import *


def takeFoodNumber(companyNameComboBox, foodName):
    liste = []
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"SELECT number FROM foodrecords WHERE name ='{foodName}'"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x[0])
    return liste[0]


def addProduct(companyNameComboBox, newFoodNumber, foodName):
    newFoodNumber = int(newFoodNumber)
    print(type(newFoodNumber))
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"UPDATE foodrecords SET number = {newFoodNumber} WHERE name = '{foodName}'"
    cursor.execute(sql)
    db.commit()


def reduceProduct(companyNameComboBox, foodNumber, foodAddNumber, foodName):
    print(foodNumber, foodAddNumber, foodName)
    if int(foodNumber) > int(foodAddNumber):
        foodNumber = int(foodNumber)
        foodNumber -= int(foodAddNumber)
    else:
        foodNumber = int(foodNumber)
        foodNumber = 0
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"UPDATE foodrecords SET number = {foodNumber} WHERE name = '{foodName}'"
    cursor.execute(sql)
    db.commit()
    print("done")
