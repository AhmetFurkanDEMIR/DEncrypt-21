from cryptosteganography import CryptoSteganography
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon
from PIL import Image
import main
import sys
import os

class Ui_Dialog(object):

    def __init__(self, a):

        self.a = a

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(666, 421)

        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 641, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(160, 90, 321, 41))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)

        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 330, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(160, 160, 151, 21))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)

        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 250, 321, 41))

        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)

        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 341, 41))

        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 200, 171, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(160, 200, 151, 21))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)

        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 330, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(310, 160, 171, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(150, 10, 341, 41))

        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(True)

        self.label_4.setFont(font)
        self.label_4.setMouseTracking(False)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 80, 341, 41))

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)

        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(150, 150, 151, 21))

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setItalic(True)

        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 150, 191, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 200, 341, 41))

        font = QtGui.QFont()
        font.setPointSize(15)
        font.setItalic(True)

        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(540, 330, 91, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 330, 91, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(150, 260, 341, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab_2, "")

        self.image_file = ("0","0")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.pushButton.setText(_translate("Dialog", "Select the image"))
        self.pushButton_3.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "Enter the text    :"))
        self.pushButton_2.setText(_translate("Dialog", "Embed text in picture"))
        self.label_2.setText(_translate("Dialog", "  Embedding encrypted text in the image"))
        self.label_3.setText(_translate("Dialog", "Enter password :"))
        self.pushButton_4.setText(_translate("Dialog", "Main menu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Embed text"))
        self.label_4.setText(_translate("Dialog", "Extract the encrypted text from the image"))
        self.pushButton_5.setText(_translate("Dialog", "Select the image"))
        self.label_5.setText(_translate("Dialog", "Enter password :"))
        self.pushButton_6.setText(_translate("Dialog", "Extract text"))
        self.pushButton_7.setText(_translate("Dialog", "Exit"))
        self.pushButton_8.setText(_translate("Dialog", "Main menu"))

        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Encrypted and embedded text will appear here when extracted.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Extract text"))

        self.pushButton_3.clicked.connect(self.exit)
        self.pushButton_7.clicked.connect(self.exit)

        self.pushButton_4.clicked.connect(self.main)
        self.pushButton_8.clicked.connect(self.main)

        self.pushButton.clicked.connect(self.image)
        self.pushButton_2.clicked.connect(self.image_run)

        self.pushButton_5.clicked.connect(self.image)
        self.pushButton_6.clicked.connect(self.run_st)


    def run_st(self):

        try:

            Image.open(self.image_file[0])

        except:

            self.pushButton_2.setText("Incorrect file type")

            return

        self.password = self.lineEdit_3.text()

        self.crypto_steganography = CryptoSteganography(self.password)

        self.secret = self.crypto_steganography.retrieve(self.image_file[0])

        if self.secret==None:

            self.pushButton_6.setText("Incorrect password")

        else:

            self.textBrowser.setText("Solved text : "+self.secret)
            self.pushButton_6.setText("Password is resolved")


    def image_run(self):

        try:

            Image.open(self.image_file[0])

        except:

            self.pushButton_2.setText("Incorrect file type")
            return

        if self.pushButton_2.text() == "Click for hidden text and image":

            self.dir = QFileDialog.getExistingDirectory(os.getenv("Desktop"))

            self.crypto_steganography.hide(self.image_file[0], str(self.dir)+"/output.png", self.text)

            self.pushButton_2.setText("Image has been indexed")

        elif self.pushButton_2.text() != "Click for hidden text and image" and self.pushButton_2.text() != "Select the image":

            self.text = self.lineEdit.text()

            self.password = self.lineEdit_2.text()

            if len(self.text)==0:

                self.pushButton_2.setText("Enter the text to be embedded")

            elif len(self.password) <= 5:

                self.pushButton_2.setText("Password length >= 6")

            else:

                self.crypto_steganography = CryptoSteganography(self.password)


                self.pushButton_2.setText("Click for hidden text and image")


    def image(self):

        self.image_file = QFileDialog.getOpenFileName(os.getenv("Desktop"))

        try:

            Image.open(self.image_file[0])

        except:

            self.pushButton_2.setText("Incorrect file type")

    def main(self):

        self.mainwin=QMainWindow()  
        self.ui=main.Ui_Dialog(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("    DEncrypt")
        self.mainwin.setFixedSize(666, 421)
        self.mainwin.move(300,100)
        self.mainwin.show() 
        self.a.hide()


    def exit(self):

        quit()
