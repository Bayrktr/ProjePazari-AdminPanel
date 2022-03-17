import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from addCategoryFunction import *
from addFoodFunction import *
from deleteFoodBackground import *
from addCategoryFunction import *


def takeFoodContentsCat(companyNameComboBox, foodName):
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"SELECT category FROM foodrecords WHERE name = '{foodName}'"
    cursor.execute(sql)
    a = cursor.fetchall()[0]
    print(a[0])
    return a[0]


def takeFoodContentsPrice(companyNameComboBox, foodName):
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"SELECT price FROM foodrecords WHERE name = '{foodName}'"
    cursor.execute(sql)
    a = cursor.fetchall()[0]
    return a[0]


def createList(companyNameComboBox, foodNameCat):
    liste = takeCategoryNames(companyNameComboBox)
    liste.remove(f"{foodNameCat}")
    liste.insert(0, f"{foodNameCat}")
    return liste


def createFoodsList(companyNameComboBox, foodName):
    liste = takeFoodNames(companyNameComboBox)
    liste.remove(f"{foodName}")
    liste.insert(0, f"{foodName}")
    return liste


def takeFoodName(companyNameComboBox):
    return takeFoodNames(companyNameComboBox)[0]


def takeFoodPrice(companyNameComboBox, foodName):
    return takeFoodContentsPrice(companyNameComboBox, foodName)


def updateFoodContents(companyNameComboBox, foodName, newFoodPrice, newFoodCategory):
    liste = ["price", "category"]
    newContents = [newFoodPrice, newFoodCategory]
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    for x, y in zip(liste, newContents):
        sql = f"UPDATE foodrecords SET {x} = '{y}' WHERE name = '{foodName}'"
        cursor.execute(sql)
        db.commit()


def deleteFoodContents(companyNameComboBox, foodName):
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"DELETE FROM foodrecords WHERE name = '{foodName}'"
    cursor.execute(sql)
    db.commit()

