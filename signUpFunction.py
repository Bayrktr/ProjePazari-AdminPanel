import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from signUpBackground import *


def openMysql():
    return mysql.connector.connect(host="127.0.0.1", user="root", password="", database="system")


def companyPassword():
    db = openMysql()
    cursor = db.cursor()
    sql = "SELECT password FROM companyrecords WHERE name = '{}'".format(str(usernameFunction()))
    cursor.execute(sql)
    for x in cursor:
        return x[0]


def companyNameList():
    liste = []
    db = openMysql()
    cursor = db.cursor()
    sql = f"SELECT name FROM companyrecords"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x[0])
    return liste


class SignUp:
    def __init__(self):
        super().__init__()
        def resultFunc():
            signUpControl = False
            self.username, self.password = usernameFunction(), passwordFunction()
            companyList = companyNameList().copy()
            print(self.username, self.password, companyList)
            if self.username in companyList:
                if self.username == "admin":
                    if self.password == companyPassword():
                        print("Admin sifresi dogru")
                        signUpControl = True
                        return signUpControl
                    else:
                        print("Admin sifresi yanlıs")
                        return signUpControl
                elif self.password == companyPassword():
                    print("{} adli hesaba giris yapildi".format(self.username))
                    signUpControl = True
                    return signUpControl
                else:
                    print("{} adli hesaba giris yapılamadı sifre yanlis".format(self.username))
                    return signUpControl
            else:
                print("{} mevcut degil.".format(self.username))
                return signUpControl
        self.result = resultFunc()

