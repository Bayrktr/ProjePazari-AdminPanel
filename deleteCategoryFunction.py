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
