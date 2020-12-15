from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
import sys
import a
import b

class Ui_Dialog(object):

    def __init__(self, a):

        self.a = a

    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")

        self.icon0 = QtGui.QPixmap('images/img1.png')
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(-10, 30, 341, 401))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        self.icon1 = QtGui.QPixmap('images/img0.png')
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 30, 341, 401))
        self.pushButton_2.setText("")

        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -4, 331, 41))

        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setMouseTracking(True)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(True)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(330, -4, 341, 41))

        font = QtGui.QFont()
        font.setFamily("Century Schoolbook L")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        self.label_2.setFont(font)
        self.label_2.setMouseTracking(True)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.label_2.raise_()

        self.pushButton_2.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):

        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "                   Image Encryption"))
        self.label_2.setText(_translate("Dialog", "  Embedding encrypted text in the image"))

        self.pushButton.setIcon(QIcon(self.icon0))
        self.pushButton.setIconSize(QtCore.QSize(250,350))

        self.pushButton_2.setIcon(QIcon(self.icon1))
        self.pushButton_2.setIconSize(QtCore.QSize(250,350))

        self.pushButton.clicked.connect(self.clicka)
        self.pushButton_2.clicked.connect(self.clickb)


    def clicka(self):

        self.mainwin=QMainWindow()  
        self.ui=b.Ui_Dialog(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("       Encrypted Image")
        self.mainwin.setFixedSize(666, 421)
        self.mainwin.move(300,100)
        self.mainwin.show() 
        self.a.hide()

    def clickb(self):

        self.mainwin=QMainWindow()  
        self.ui=a.Ui_Dialog(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("       Encrypted Text")
        self.mainwin.setFixedSize(666, 421)
        self.mainwin.move(300,100)
        self.mainwin.show() 
        self.a.hide()



def init():

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("    DEncrypt")
    Dialog.setFixedSize(666, 421)
    Dialog.move(300,100)
    Dialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    init()
