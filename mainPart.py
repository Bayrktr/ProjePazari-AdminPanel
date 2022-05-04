import re
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
from deleteUserBackground import *
from deleteUserFunction import *
from menuOptionsBackground import *
from menuOptionsFunction import menuRecordFunction
from menuSelectFunction import *
from menuSelectBackground import *


class signInPart(QWidget):
    def __init__(self):
        super().__init__()
        signInBackground(self)
        buttonFunction().clicked.connect(self.singnUpControl)

    def singnUpControl(self):
        if SignUp().result:
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
        deleteUserFunction().clicked.connect(self.deleteUserOpen)
        menuOptionsFunction().clicked.connect(self.menuOptionsOpen)
        menuSelectButtonFunction().clicked.connect(self.menuSelectOpen)

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
            if len(takeFoodNames(companyNameComboBox)) != 0:
                foodName = takeFoodName(companyNameComboBox)
                foodNumber = takeFoodNumber(companyNameComboBox, foodName)
                foodName = takeFoodNames(companyNameComboBox)
                self.addProductWindow = addProductPart()
                self.addProductWindow.show()

    def addUserOpen(self):
        self.addUserWindow = addUserPart()
        self.addUserWindow.show()

    def deleteUserOpen(self):
        global newUserPassword, newUserMail, userList
        if len(takeUsers()) != 0:
            userName = firstName()
            liste = userDataText(userName)
            newUserPassword, newUserMail = liste[0], liste[1]
            userList = creatingList()
            self.deleteUserWindow = deleteUserPart()
            self.deleteUserWindow.show()

    def menuOptionsOpen(self):
        self.menuOptionsWindow = menuOptionsPart()
        self.menuOptionsWindow.show()

    def menuSelectOpen(self):
        companyNameComboBox = comboBoxFunction().currentText()
        if allMenuNames(companyNameComboBox) != 0:
            self.menuSelectWindow = menuSelectPart()
            self.menuSelectWindow.show()


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
        userName, userPassword, userMail = addUserNameText(), addUserPasswordText(), addUserMailText()
        if mailCheck(userMail):
            if userName not in takeUsers() and userMail not in takeUserMails():
                userRecord(userName, userPassword, userMail)


class deleteUserPart(QWidget):
    def __init__(self):
        super().__init__()
        global newUserPassword, newUserMail, userList
        deleteUsersBackground(self, newUserPassword, newUserMail, userList)
        deleteUserButtonFunction().clicked.connect(self.delete)
        updateUserButtonFunction().clicked.connect(self.update)
        usersComboBoxFunction().activated.connect(self.refleshTwo)

    def refleshTwo(self):
        global newUserPassword, newUserMail, userList
        userList = usersComboBoxFunction().currentText()
        userName = takeNameFromList(userList)
        userList = createListForReflesh(userList)
        liste = userDataText(userName)
        newUserPassword, newUserMail = liste[0], liste[1]
        self.reflesh()

    def delete(self):
        global newUserPassword, newUserMail, userList
        users = usersComboBoxFunction().currentText()
        userName = takingArgForDelete(users)[0]
        deleteUser(userName)
        userList.remove(f"{users}")
        if len(userList) == 0:
            self.close()
        else:
            liste = userList[0]
            liste = takingArgForDelete(liste)
            newUserPassword, newUserMail = liste[1], liste[2]
            self.reflesh()

    def update(self):
        global newUserPassword, newUserMail
        userName = usersComboBoxFunction().currentText()
        userName = takingArgForDelete(userName)[0]
        newUserPassword, newUserMail = newUserPasswordLineText(), newUserMailLineText()
        updateUsers(newUserPassword, newUserMail, userName)
        self.reflesh()

    def reflesh(self):
        self.close()
        self.deleteUserWindow = deleteUserPart()
        self.deleteUserWindow.show()


class menuOptionsPart(QWidget):
    def __init__(self):
        super().__init__()
        companyNameComboBox = comboBoxFunction().currentText()
        menuOptionsBackground(self, companyNameComboBox)
        menuRecordButtonFunction().clicked.connect(self.menuRecord)

    def menuRecord(self):
        companyNameComboBox = comboBoxFunction().currentText()
        menuName, height, widght, fontColor, titleColor, fontType, fontSize, titleSize, categoryBetween, startX, startY, fontBetweenSize, titleBetweenSizeX, titleBetweenSizeY, priceColor, unitName = menuNameText(), menuHeightText(), menuWidghtText(), fontColorText(), titleColorText(), fontTypeText(), startXText(), startYText(), categoryBetweenText(), fontSizeText(), titleSizeText(), fontBetweenSizeText(), titleBetweenSizeXText(), titleBetweenSizeYText(), priceColorText(), unitNameText()
        if menuName not in allMenuNames(companyNameComboBox):
            noneStrList = [str(height), str(widght), str(startX), str(startY), str(categoryBetween), str(fontSize),
                           str(titleSize), str(fontBetweenSize), str(titleBetweenSizeX), str(titleBetweenSizeY)]
            noneIntList = [str(fontColor), str(titleColor), str(priceColor), str(unitName),
                           str(fontType)]
            flag = True
            for x in noneStrList:
                if len(re.findall("\D+", x)) != 0 or len(re.findall("\s", x)) != 0:
                    flag = False
                    break
            for x in noneIntList:
                if len(re.findall("\d+", x)) != 0 or len(re.findall("\s", x)) != 0:
                    flag = False
                    break
            if flag:
                menuDatas = [str(menuName), str(height), str(widght), str(fontColor), str(titleColor), str(fontType),
                             str(startX), str(startY), str(categoryBetween), str(fontSize), str(titleSize),
                             str(fontBetweenSize), str(titleBetweenSizeX), str(titleBetweenSizeY), str(priceColor),
                             str(unitName)]
                menuRecordFunction(menuDatas, companyNameComboBox)
                self.reflesh()

    def reflesh(self):
        self.close()
        self.menuOptionsWindow = menuOptionsPart()
        self.menuOptionsWindow.show()


class menuSelectPart(QWidget):
    def __init__(self):
        super().__init__()
        self.companyNameComboBox = comboBoxFunction().currentText()
        companyNameComboBox = self.companyNameComboBox
        selectMenuBackground(self, companyNameComboBox)
        deleteMenuButtonFunction().clicked.connect(self.deleteMenu)
        selectMenuButtonFunction().clicked.connect(self.selectMenu)

    def deleteMenu(self):
        menuName = selectMenuNameComboBoxFunction().currentText()
        companyNameComboBox = self.companyNameComboBox
        deleteMenu(menuName, companyNameComboBox)
        self.reflesh()

    def selectMenu(self):
        menuName = selectMenuNameComboBoxFunction().currentText()
        companyNameComboBox = self.companyNameComboBox
        selectMenuFunc(menuName, companyNameComboBox)

    def reflesh(self):
        self.close()
        self.menuSelectWindow = menuSelectPart()
        self.menuSelectWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    adminWindow = adminPart()
    signInWindow = signInPart()
    signInWindow.show()
    app.exec_()
