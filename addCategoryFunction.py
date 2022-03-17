import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from adminBackground import *
from adminFunction import *
from mainPart import *

categoryNameList = ["name", "code", "crdate"]


def connectToCompanyDataDb(companyNameComboBox):
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database=f"{companyNameComboBox}")


def takeCategoryNames(companyNameComboBox):
    liste = []
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = "SELECT name FROM categoryrecords"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        liste.append(x[0])
    return liste


def takaData(x, companyNameComboBox):
    liste = []
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"SELECT * FROM categoryrecords WHERE name = '{x}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        liste.append(x)
    print(liste)
    return liste[0]


def addCategory(categoryNameText, companyNameComboBox):
    if categoryNameText not in takeCategoryNames(companyNameComboBox):
        db = connectToCompanyDataDb(companyNameComboBox)
        cursor = db.cursor()
        sql = f"INSERT INTO categoryrecords (name,code,crdate) VALUES ('{categoryNameText}','{createCode()}','{timeSettings()}')"
        cursor.execute(sql)
        db.commit()
