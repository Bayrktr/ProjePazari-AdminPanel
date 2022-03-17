import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from signUpFunction import *


def openMysql():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database="system")


def connectUser():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="")


def takeData(x):
    liste = []
    db = openMysql()
    cursor = db.cursor()
    sql = f"SELECT {x} FROM companyrecords"
    cursor.execute(sql)
    a = cursor.fetchall()
    for x in a:
        liste.append(x[0])
    return liste


def createCode(alphabet=string.ascii_lowercase, numbers=string.digits):
    a = 0
    liste = []
    alphabet = list(alphabet)
    numbers = list(numbers)
    alphabet = alphabet + numbers
    while a < 12:
        a += 1
        liste.append(random.choice(alphabet))
    return "".join(liste)


def timeSettings(now=datetime.today()):
    timeNow = []
    timeNow.append(str(now.year)), timeNow.append(str(now.month)), timeNow.append(str(now.day)), timeNow.append(
        str(now.hour)), timeNow.append(str(now.minute))
    return ".".join(timeNow)


def takeIp():
    return socket.gethostbyname(socket.gethostname())
