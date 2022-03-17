import random
import re
import socket
import string
import sys
from datetime import datetime
import mysql.connector
from PyQt5.QtCore import QRect, QPropertyAnimation
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QMainWindow, QLabel, QComboBox
from signUpBackground import *
from signUpFunction import *
from adminBackground import *
from registerCompanyBackground import *
from registerCompanyFunction import *
from deleteFunction import *
from addCategoryBackground import *
from addFoodBackground import *
from deleteFoodBackground import *
from deleteFoodFunction import *
from deleteCategoryBackground import *
from deleteCategoryFunction import *
from addProductBackground import *
from addProductFunction import *
from addUserBackground import *
from addUserFunction import *


class signInPart(QWidget):
    def __init__(self):
        super().__init__()
        signInBackground(self)
        buttonFunction().clicked.connect(self.singnUpControl)

    def singnUpControl(self):
        if SignUp().result == True:
            signInWindow.destroy()
            adminWindow.show()


class adminPart(QMainWindow):
    def __init__(self):
        super().__init__()
        adminBackground(self)
        data(self)
        registerButtonFunction().clicked.connect(self.openRegisterCompany)
        refleshButtonFunction().clicked.connect(self.reflesh)
        deleteButtonFunction().clicked.connect(self.deleteCompany)
        addCategoryButtonFunction().clicked.connect(self.addCategoryOpen)
        addFoodButtonFunction().clicked.connect(self.addFoodOpen)
        deleteFoodsButtonFunction().clicked.connect(self.deleteFoodOpen)
        deleteCategoryFunction().clicked.connect(self.deleteCategoryOpen)
        addProductFunction().clicked.connect(self.addProductOpen)
        addUserButtonFunction().clicked.connect(self.addUserOpen)

    def openRegisterCompany(self):
        self.registerWindow = registerPart()
        self.registerWindow.show()

    def reflesh(self):
        self.close()
        self.adminWindow = adminPart()
        self.adminWindow.show()

    def deleteCompany(self):
        companyNameComboBox = comboBoxFunction().currentText()
        if companyNameComboBox != "":
            Delete()
            self.reflesh()

    def addCategoryOpen(self):
        companyNameComboBox = comboBoxFunction().currentText()
        if companyNameComboBox != "":
            self.addCategoryWindow = addCategoryPart()
            self.addCategoryWindow.show()

    def addFoodOpen(self):
        companyNameComboBox = comboBoxFunction().currentText()
        if companyNameComboBox != "":
            self.addFoodWindow = addFoodPart()
            self.addFoodWindow.show()

    def deleteFoodOpen(self):
        global foodName, foodPrice, foodNameCat
        companyNameComboBox = comboBoxFunction().currentText()
        if companyNameComboBox != "":
            if len(takeFoodNames(companyNameComboBox)) != 0:
                foodName = takeFoodName(companyNameComboBox)
                foodPrice = takeFoodPrice(companyNameComboBox, foodName)
                foodNameCat = takeFoodContentsCat(companyNameComboBox, foodName)
                foodNameCat = createList(companyNameComboBox, foodNameCat)
                foodName = createFoodsList(companyNameComboBox, foodName)
                if len(takeFoodNames(companyNameComboBox)) != 0:
                    self.deleteFoodWindow = deleteFoodPart()
                    self.deleteFoodWindow.show()

    def deleteCategoryOpen(self):
        companyNameComboBox = comboBoxFunction().currentText()
        if companyNameComboBox != "":
            self.deleteCategoryWindow = deleteCategoryPart()
            self.deleteCategoryWindow.show()

    def addProductOpen(self):
        global foodName, foodNumber
        companyNameComboBox = comboBoxFunction().currentText()
        if companyNameComboBox != "":
            if takeFoodNames(companyNameComboBox) != []:
                foodName = takeFoodName(companyNameComboBox)
                foodNumber = takeFoodNumber(companyNameComboBox, foodName)
                foodName = takeFoodNames(companyNameComboBox)
                self.addProductWindow = addProductPart()
                self.addProductWindow.show()

    def addUserOpen(self):
        if comboBoxFunction().currentText() != "":
            self.addUserWindow = addUserPart()
            self.addUserWindow.show()


class registerPart(QWidget):
    def __init__(self):
        super().__init__()
        registerBackground(self)
        registerButton().clicked.connect(self.registerFunc)

    def registerFunc(self):
        Register()
        adminWindow.close()
        self.adminWindow = adminPart()
        self.adminWindow.show()


class addCategoryPart(QWidget):
    def __init__(self):
        super().__init__()
        global comboBoxName, companyNameComboBox
        addCategoryBackground(self)
        companyNameComboBox = comboBoxFunction().currentText()
        mainData(self, companyNameComboBox)
        addCategoryRecordFunction().clicked.connect(self.addCategoryRecord)

    def comboBoxFunc(self):
        global comboBoxName
        comboBoxName = comboBoxFunction()
        return comboBoxName

    def addCategoryRecord(self):
        categoryNameText = categoryNameFunction()
        addCategory(categoryNameText, companyNameComboBox)
        self.reflesh()

    def reflesh(self):
        self.close()
        self.addCategoryWindow = addCategoryPart()
        self.addCategoryWindow.show()


class addFoodPart(QWidget):
    def __init__(self):
        super().__init__()
        global comboBoxName, companyNameComboBox
        companyNameComboBox = comboBoxFunction().currentText()
        addFoodsBackground(self, companyNameComboBox)
        mainDataFood(self, companyNameComboBox)
        recordFoodButton().clicked.connect(self.recordFood)

    def comboBoxFunc(self):
        global comboBoxName
        comboBoxName = comboBoxFunction()
        return comboBoxName

    def recordFood(self):
        global companyNameComboBox
        foodName, foodPrice, selectCategoryName = foodNameText().displayText(), foodPriceText().displayText(), selectCategoryComboBoxFunc().currentText()
        foodsRecord(foodName, foodPrice, companyNameComboBox, selectCategoryName)
        self.reflesh()

    def reflesh(self):
        self.close()
        self.addFoodWindow = addFoodPart()
        self.addFoodWindow.show()


class deleteFoodPart(QWidget):
    def __init__(self):
        super().__init__()
        global companyNameComboBox, foodNameCat, foodPrice, foodName
        companyNameComboBox = comboBoxFunction().currentText()
        print("sa")
        print(foodNameCat, foodPrice, foodName)
        deleteFoodsBackground(self, companyNameComboBox, foodNameCat, foodPrice, foodName)
        foodListComboBoxFunction().activated.connect(self.reflesh)
        updateFoodFunction().clicked.connect(self.updateFood)
        deleteFoodFunction().clicked.connect(self.deleteFood)

    def reflesh(self):
        self.foodListActivate(companyNameComboBox)
        self.close()
        self.deleteFoodWindow = deleteFoodPart()
        self.deleteFoodWindow.show()

    def updateFood(self):
        foodName = foodListComboBoxFunction().currentText()
        newFoodPrice = newPriceFunction().displayText()
        newFoodCategory = foodCategoryFunction().currentText()
        updateFoodContents(companyNameComboBox, foodName, newFoodPrice, newFoodCategory)
        self.reflesh()

    def deleteFood(self):
        foodName = foodListComboBoxFunction().currentText()
        deleteFoodContents(companyNameComboBox, foodName)
        self.refleshAfterDelete()

    def foodListActivate(self, companyNameComboBox):
        global foodName, foodNameCat, foodPrice
        foodName = foodListComboBoxFunction().currentText()
        foodNameCat = takeFoodContentsCat(companyNameComboBox, foodName)
        foodNameCat = createList(companyNameComboBox, foodNameCat)
        foodPrice = takeFoodContentsPrice(companyNameComboBox, foodName)
        foodName = createFoodsList(companyNameComboBox, foodName)

    def refleshAfterDelete(self):
        global foodName, foodPrice, foodNameCat
        if len(takeFoodNames(companyNameComboBox)) != 0:
            foodName = takeFoodName(companyNameComboBox)
            foodPrice = takeFoodPrice(companyNameComboBox, foodName)
            foodNameCat = takeFoodContentsCat(companyNameComboBox, foodName)
            foodNameCat = createList(companyNameComboBox, foodNameCat)
            foodName = createFoodsList(companyNameComboBox, foodName)
            self.close()
            self.deleteFoodWindow = deleteFoodPart()
            self.deleteFoodWindow.show()
        else:
            self.close()


class deleteCategoryPart(QWidget):
    def __init__(self):
        super().__init__()
        global companyNameComboBox
        companyNameComboBox = comboBoxFunction().currentText()
        print(companyNameComboBox)
        deleteCategorysBackground(self, companyNameComboBox)
        deleteCategoryButtonFunction().clicked.connect(self.delete)

    def delete(self):
        categoryName = selectDelCategoryFunction().currentText()
        deleteCategory(companyNameComboBox, categoryName)
        self.reflesh()

    def reflesh(self):
        self.close()
        self.deleteCategoryWindow = deleteCategoryPart()
        self.deleteCategoryWindow.show()


class addProductPart(QWidget):
    def __init__(self):
        super().__init__()
        global companyNameComboBox, foodName, foodNumber
        companyNameComboBox = comboBoxFunction().currentText()
        print(companyNameComboBox, foodName, foodNumber)
        addProductsBackground(self, foodName, foodNumber)
        selectFoodProductFunction().activated.connect(self.reflesh)
        addProductButtonFunction().clicked.connect(self.addProduct)
        reduceProductFunction().clicked.connect(self.reduceProduct)

    def reflesh(self):
        global companyNameComboBox, foodName, foodNumber
        foodName = selectFoodProductFunction().currentText()
        foodNumber = takeFoodNumber(companyNameComboBox, foodName)
        foodName = createFoodsList(companyNameComboBox, foodName)
        self.close()
        self.addProductWindow = addProductPart()
        self.addProductWindow.show()

    def addProduct(self):
        global foodNumber
        foodAddNumber = addProductTextFunction()
        newFoodNumber = int(foodNumber) + int(foodAddNumber)
        if len(re.findall("\D+", str(foodAddNumber))) == 0:
            foodName = selectFoodProductFunction().currentText()
            addProduct(companyNameComboBox, newFoodNumber, foodName)
            self.reflesh()

    def reduceProduct(self):
        global foodNumber
        foodAddNumber = addProductTextFunction()
        if len(re.findall("\D+", str(foodAddNumber))) == 0:
            foodName = selectFoodProductFunction().currentText()
            print(foodName)
            reduceProduct(companyNameComboBox, foodNumber, foodAddNumber, foodName)
            self.reflesh()


class addUserPart(QWidget):
    def __init__(self):
        super().__init__()
        addUsersBackground(self)
        addUserRegisterButtonFunction().clicked.connect(self.record)

    def record(self):
        companyNameComboBox = comboBoxFunction().currentText()
        userName, userPassword, userMail = addUserNameText(), addUserPasswordText(), addUserMailText()
        if mailCheck(userMail):
            if userName not in takeUsers(companyNameComboBox) and userMail not in takeUserMails(companyNameComboBox):
                userRecord(companyNameComboBox, userName, userPassword, userMail)


class deleteUserPart(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    adminWindow = adminPart()
    signInWindow = signInPart()
    signInWindow.show()
    app.exec_()
