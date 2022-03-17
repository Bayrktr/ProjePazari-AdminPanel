import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from registerCompanyBackground import *
from signUpFunction import *
from adminFunction import *
from mainPart import *


def connectToCompanyDataDb(companyName):
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database=f"{companyName}")


def mailCheck():
    if str(companyMailText()).endswith('@gmail.com') == True or str(companyMailText()).endswith('@outlook.com') == True:
        return True
    else:
        return False


def companyMailList(db=openMysql()):
    liste = []
    cursor = db.cursor()
    sql = f"SELECT mail FROM companyrecords"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x[0])
    return liste


def recordCompany(companyName, companyMail, companyPasswrd, code=createCode()):
    def createTables():
        db = connectToCompanyDataDb(companyName)
        cursor = db.cursor()
        sql = "CREATE TABLE foodrecords (name TEXT,price TEXT,category TEXT,code TEXT,number INT,crdate DATE)"
        cursor.execute(sql)
        sql = "CREATE TABLE categoryrecords (name TEXT,code TEXT,crdate DATE)"
        cursor.execute(sql)
        sql = "CREATE TABLE userrecords (name TEXT,password TEXT,mail TEXT,crdate DATE)"
        cursor.execute(sql)
        recordToSystem()

    def createDb():
        db = connectUser()
        cursor = db.cursor()
        sql = f"CREATE DATABASE {companyName}"
        cursor.execute(sql)
        createTables()

    def recordToSystem(db=openMysql()):
        print(companyName, companyPasswrd, companyMail)
        cursor = db.cursor()
        sql = f"INSERT INTO companyrecords (name,password,code,mail,activity,fromip,crdate) VALUES ('{companyName}','{companyMail}','{code}','{companyPasswrd}','1','{takeIp()}','{timeSettings()}')"
        cursor.execute(sql)
        db.commit()

    createDb()


class Register:
    def __init__(self):
        super().__init__()

        def registerFunc():
            companyName, companyPasswrd, companyMail = companyNameText(), companyPasswordText(), companyMailText()
            if companyName not in companyNameList():
                if mailCheck() == True and companyMail not in companyMailList():
                    recordCompany(companyName, companyPasswrd, companyMail)
                    print("{} adlı şirket mevcut degıl olusturuluyor...".format(companyName))

        registerFunc()
