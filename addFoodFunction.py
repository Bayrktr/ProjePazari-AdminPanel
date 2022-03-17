import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from adminFunction import *
from addCategoryFunction import *


def takeDataFood(x, companyNameComboBox):
    liste = []
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"SELECT {x} FROM foodrecords"
    cursor.execute(sql)
    a = cursor.fetchall()
    for x in a:
        liste.append(x[0])
    return liste


def takeFoodNames(companyNameComboBox):
    liste = []
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = "SELECT name FROM foodrecords"
    cursor.execute(sql)
    for x in cursor:
        liste.append(x[0])
    return liste


def foodsRecord(foodName, foodPrice, companyNameComboBox, selectCategoryName):
    if foodPrice == "" or foodName == "":
        print("Bos deger")
    else:
        result = len(re.findall("\D+", str(foodPrice)))
        if companyNameComboBox in companyNameList():
            if foodName not in takeFoodNames(companyNameComboBox) and result == 0:
                db = connectToCompanyDataDb(companyNameComboBox)
                cursor = db.cursor()
                sql = f"INSERT INTO foodrecords (name,price,category,code,number,crdate) VALUES ('{foodName}','{foodPrice}','{selectCategoryName}','{createCode()}','0','{timeSettings()}')"
                cursor.execute(sql)
                db.commit()
