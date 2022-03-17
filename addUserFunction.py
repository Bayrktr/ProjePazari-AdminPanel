import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from adminFunction import *
from addCategoryFunction import *
from adminFunction import *


def takeUsers(companyNameComboBox):
    liste = []
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"SELECT name FROM userrecords"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x[0])
    return liste


def takeUserMails(companyNameComboBox):
    liste = []
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"SELECT mail FROM userrecords"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x[0])
    return liste


def userRecord(companyNameComboBox, userName, userPassword, userMail):
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"INSERT INTO userrecords (name, password,mail,crdate) VALUES ('{userName}','{userPassword}','{userMail}','{timeSettings()}')"
    cursor.execute(sql)
    db.commit()


def mailCheck(userMail):
    return str(userMail).endswith("gmail.com") or str(userMail).endswith("outlook.com") or str(userMail).endswith(
        "hotmail.com")
