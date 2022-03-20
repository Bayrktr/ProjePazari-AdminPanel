import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from addCategoryFunction import *


def takeNameFromList(userList):
    liste = str(userList).split(3 * " ")
    liste.pop(len(liste) - 1)
    liste = liste[0]
    return liste


def deleteUser(userList, companyNameComboBox):
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"DELETE FROM userrecords WHERE name = '{userList}'"
    cursor.execute(sql)
    db.commit()


def userDataText(companyNameComboBox, userName):
    liste = []
    words = ["password", "mail"]
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    for x in words:
        sql = f"SELECT {x} FROM userrecords WHERE name = '{userName}'"
        cursor.execute(sql)
        for x in cursor.fetchone():
            liste.append(x)
    return liste


def firstName(companyNameComboBox):
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = "SELECT name FROM userrecords"
    cursor.execute(sql)
    return cursor.fetchone()[0]


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


def createListForReflesh(companyNameComboBox, userList):
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
    liste.remove(f"{userList}")
    liste.insert(0, f"{userList}")
    return liste


def takingArgForDelete(liste):
    liste = str(liste).split(3 * " ")
    return liste


def updateUsers(companyNameComboBox, newUserPassword, newUserMail, userName):
    words = ["password", "mail"]
    arg = [newUserPassword, newUserMail]
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    for x, y in zip(words, arg):
        sql = f"UPDATE userrecords SET {x} = '{y}' WHERE name = '{userName}'"
        cursor.execute(sql)
        db.commit()
