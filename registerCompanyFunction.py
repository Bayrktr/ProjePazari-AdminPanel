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
    if str(companyMailText()).endswith('@gmail.com') or str(companyMailText()).endswith('@outlook.com'):
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
        sql = "CREATE TABLE foodhistory (person TEXT,names TEXT,numbers TEXT,desknumber TEXT,crdate DATE)"
        cursor.execute(sql)
        sql = "CREATE TABLE menuOptions (name TEXT, height TEXT,widght TEXT, fontColor TEXT, titleColor TEXT ,fontType TEXT,fontSize TEXT,titleSize TEXT,categoryBetween TEXT,startX TEXT,startY TEXT,fontBetweenSize TEXT,titleBetweenSizeX TEXT,titleBetweenSizeY TEXT,priceColor TEXT,unitName TEXT,crdate DATE)"
        cursor.execute(sql)
        recordToSystem()

    def createDb():
        db = connectUser()
        cursor = db.cursor()
        sql = f"CREATE DATABASE {companyName}"
        cursor.execute(sql)
        db.commit()
        createTables()

    def recordToSystem(db=openMysql()):
        cursor = db.cursor()
        sql = f"INSERT INTO companyrecords (name,password,code,mail,activity,fromip,crdate) VALUES ('{companyName}','{companyMail}','{code}','{companyPasswrd}','1','{takeIp()}','{timeSettings()}')"
        cursor.execute(sql)
        db.commit()

    createDb()


class Register:
    def __init__(self):
        super().__init__()
        self.registerFunc()

    def registerFunc(self):
        companyName, companyPasswrd, companyMail = companyNameText(), companyPasswordText(), companyMailText()
        if companyName not in companyNameList():
            if mailCheck() and companyMail not in companyMailList():
                recordCompany(companyName, companyPasswrd, companyMail)
                print("{} adlı şirket mevcut degıl olusturuluyor...".format(companyName))
