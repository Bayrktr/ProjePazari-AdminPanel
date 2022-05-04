import mysql.connector
from addCategoryFunction import *


def allMenuNames(companyNameComboBox):
    liste = []
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = "SELECT name FROM menuoptions"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x[0])
    db.close()
    return liste


def deleteMenu(menuName, companyNameComboBox):
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = f"DELETE FROM menuoptions WHERE name = '{menuName}'"
    cursor.execute(sql)
    db.commit()
    db.close()


def selectMenuFunc(menuName, companyNameComboBox):
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    menuNamesList = allMenuNames(companyNameComboBox)
    menuNamesList.remove(str(menuName))
    for x in menuNamesList:
        sql = f"UPDATE menuoptions SET flag = '0' WHERE name = '{x}'"
        cursor.execute(sql)
    sql = f"UPDATE menuoptions SET flag = '1' WHERE name = '{str(menuName)}'"
    cursor.execute(sql)
    db.commit()
    db.close()
