import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from adminFunction import timeSettings
from addCategoryFunction import *

def menuRecordFunction(menuDatas, companyNameComboBox):
    arg = ['name', 'height', 'widght', 'fontColor', 'titleColor', 'fontType', 'fontSize', 'titleSize',
           'categoryBetween', 'startX', 'startY', 'fontBetweenSize', 'titleBetweenSizeX', 'titleBetweenSizeY',
           'priceColor', 'unitName',
           'flag', 'crdate']
    argWords = ",".join(arg)
    menuDatas.append("0")
    menuDatas.append("{}".format(timeSettings()))
    word = ""
    for x in menuDatas:
        word += "'{}' ".format(x)
    word = word.split()
    word = ",".join(word)
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"INSERT INTO menuoptions ({argWords}) VALUES ({word})"
    cursor.execute(sql)
    db.commit()
