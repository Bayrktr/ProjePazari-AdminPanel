import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from adminBackground import *
from adminFunction import *


class Delete():
    def __init__(self):
        super().__init__()

        def deleteFunc():
            companyName = comboBoxFunction().currentText()
            print(companyName)

            def deleteDb(db=connectUser()):
                cursor = db.cursor()
                sql = f"DROP DATABASE {companyName}"
                cursor.execute(sql)

            def deleteFromTable(db=openMysql()):
                cursor = db.cursor()
                sql = f"DELETE FROM companyrecords WHERE name = '{companyName}'"
                cursor.execute(sql)
                db.commit()

            deleteDb()
            deleteFromTable()

        deleteFunc()
