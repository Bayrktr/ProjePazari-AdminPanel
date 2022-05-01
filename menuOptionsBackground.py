from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QComboBox
from addCategoryFunction import connectToCompanyDataDb
from PyQt5.QtGui import QFont, QIcon, QPixmap


def menuOptionsBackground(self, companyNameComboBox):
    global menuName, menuHeight, menuWidght, fontColor, titleColor, fontType, startX, startY, categoryBetween, fontSize, titleSize, fontBetweenSize, titleBetweenSizeX, titleBetweenSizeY, priceColor, unitName, menuRecordButton
    self.setFixedSize(800, 600)
    self.setWindowTitle("RegisterCompany")
    self.setStyleSheet("background-color: gray")
    menuName = QLineEdit("Menu Name", self)
    menuName.setGeometry(10, 10, 100, 40)
    menuName.setStyleSheet("background-color: orange")
    menuHeight = QLineEdit("Height", self)
    menuHeight.setGeometry(10, 60, 100, 40)
    menuHeight.setStyleSheet("background-color: orange")
    menuWidght = QLineEdit("Weight", self)
    menuWidght.setGeometry(10, 110, 100, 40)
    menuWidght.setStyleSheet("background-color: orange")
    fontColor = QLineEdit("FontColor", self)
    fontColor.setGeometry(10, 160, 100, 40)
    fontColor.setStyleSheet("background-color: orange")
    titleColor = QLineEdit("TitleColor", self)
    titleColor.setGeometry(10, 210, 100, 40)
    titleColor.setStyleSheet("background-color: orange")
    fontType = QLineEdit("FontType", self)
    fontType.setGeometry(10, 260, 100, 40)
    fontType.setStyleSheet("background-color: orange")
    startX = QLineEdit("startX", self)
    startX.setGeometry(10, 310, 100, 40)
    startX.setStyleSheet("background-color: orange")
    startY = QLineEdit("startY", self)
    startY.setGeometry(10, 360, 100, 40)
    startY.setStyleSheet("background-color: orange")
    categoryBetween = QLineEdit("categoryBetween", self)
    categoryBetween.setGeometry(10, 410, 100, 40)
    categoryBetween.setStyleSheet("background-color: orange")
    fontSize = QLineEdit("FontSize", self)
    fontSize.setGeometry(10, 460, 100, 40)
    fontSize.setStyleSheet("background-color: orange")
    titleSize = QLineEdit("TitleSize", self)
    titleSize.setGeometry(10, 510, 100, 40)
    titleSize.setStyleSheet("background-color: orange")
    fontBetweenSize = QLineEdit("FontBetweenSize", self)
    fontBetweenSize.setGeometry(10, 560, 100, 40)
    fontBetweenSize.setStyleSheet("background-color: orange")
    titleBetweenSizeX = QLineEdit("TitleBetweenSizeX", self)
    titleBetweenSizeX.setGeometry(120, 160, 100, 40)
    titleBetweenSizeX.setStyleSheet("background-color: orange")
    titleBetweenSizeY = QLineEdit("TitleBetweenSizeY", self)
    titleBetweenSizeY.setGeometry(120, 210, 100, 40)
    titleBetweenSizeY.setStyleSheet("background-color: orange")
    priceColor = QLineEdit("PriceColor", self)
    priceColor.setGeometry(120, 260, 100, 40)
    priceColor.setStyleSheet("background-color: orange")
    unitName = QLineEdit("UnitName", self)
    unitName.setGeometry(120, 310, 100, 40)
    unitName.setStyleSheet("background-color: orange")
    menuRecordButton = QPushButton("Record", self)
    menuRecordButton.setGeometry(120, 360, 100, 40)
    menuRecordButton.setStyleSheet("background-color: orange")
    menuStartX = 300
    menuStartY = 10
    for x in menuTexts(companyNameComboBox)[0]:
        text = QLabel(f"{x}", self)
        text.setGeometry(menuStartX, menuStartY, 400, 30)
        text.setStyleSheet("color: yellow;")
        text.setFont(QFont('Times New Roman', 5))
        menuStartY += 30


def menuTexts(companyNameComboBox):
    liste = []
    newList = []
    bigList = []
    db = connectToCompanyDataDb(companyNameComboBox)
    cursor = db.cursor()
    sql = "SELECT * FROM menuoptions"
    cursor.execute(sql)
    for x in cursor.fetchall():
        liste.append(x)
        for x in liste:
            newList.append(x)
        bigList.append(newList)
        liste = []
        newList = []
    print(liste)
    db.close()
    return bigList


def menuNameText():
    global menuName
    return menuName.displayText()


def menuHeightText():
    global menuHeight
    return menuHeight.displayText()


def menuWidghtText():
    global menuWidght
    return menuWidght.displayText()


def fontColorText():
    global fontColor
    return fontColor.displayText()


def titleColorText():
    global titleColor
    return titleColor.displayText()


def fontTypeText():
    global fontType
    return fontType.displayText()


def startXText():
    global startX
    return startX.displayText()


def startYText():
    global startY
    return startY.displayText()


def categoryBetweenText():
    global categoryBetween
    return categoryBetween.displayText()


def fontSizeText():
    global fontSize
    return fontSize.displayText()


def titleSizeText():
    global titleSize
    return titleSize.displayText()


def fontBetweenSizeText():
    global fontBetweenSize
    return fontBetweenSize.displayText()


def titleBetweenSizeXText():
    global titleBetweenSizeX
    return titleBetweenSizeX.displayText()


def titleBetweenSizeYText():
    global titleBetweenSizeY
    return titleBetweenSizeY.displayText()


def priceColorText():
    global priceColor
    return priceColor.displayText()


def unitNameText():
    global unitName
    return unitName.displayText()


def menuRecordButtonFunction():
    global menuRecordButton
    return menuRecordButton
