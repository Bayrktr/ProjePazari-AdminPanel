import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from addCategoryFunction import *
from adminFunction import timeSettings


def menuRecordFunction(noneStrList, companyNameComboBox):
    print(noneStrList)
    print(len(noneStrList))
    word = ""
    for x in noneStrList:
        word += "'{}',".format(x)

    print(word)
    arg = ['height', 'widght', 'startX', 'startY', 'categoryBetween', 'fontSize', 'titleSize', 'fontBetweenSize',
           'fontBetweenSizeX', 'fontBetweenSizeY', 'name', 'fontColor', 'titleColor', 'priceColor', 'unitName',
           'fontType',
           'crdate']
    print(len(arg))
    arg = ",".join(arg)
    print(arg)
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"INSERT INTO menuoptions ({arg}) VALUES ({word}'{timeSettings()}')"
    cursor.execute(sql)
    db.commit()
