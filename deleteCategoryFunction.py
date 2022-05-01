import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from addCategoryFunction import *


def deleteCategory(companyNameComboBox, categoryName):
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"DELETE FROM  categoryrecords WHERE name = '{categoryName}'"
    cursor.execute(sql)
    db.commit()
    deleteSomeFoods(db, cursor, categoryName)


def deleteSomeFoods(db, cursor, categoryName):
    def delete(db, cursor, liste):
        for x in liste:
            sql = f"DELETE FROM foodrecords WHERE name = '{x}'"
            cursor.execute(sql)
            db.commit()

    liste = []
    sql = f"SELECT * FROM foodrecords WHERE category = '{categoryName}'"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x[0])
    delete(db, cursor, liste)
