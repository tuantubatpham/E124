# Form implementation generated from reading ui file 'C:\Users\Quoc Vinh\Downloads\E124\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(489, 453)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(15, 11, 461, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton2001 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton2001.setGeometry(QtCore.QRect(30, 406, 61, 21))
        self.pushButton2001.setObjectName("pushButton2001")
        self.pushButtontop3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtontop3.setGeometry(QtCore.QRect(140, 410, 61, 21))
        self.pushButtontop3.setObjectName("pushButtontop3")
        self.pushButtonrole = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonrole.setGeometry(QtCore.QRect(250, 410, 71, 21))
        self.pushButtonrole.setObjectName("pushButtonrole")
        self.pushButtoncount = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtoncount.setGeometry(QtCore.QRect(385, 410, 71, 21))
        self.pushButtoncount.setObjectName("pushButtoncount")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton2001.setText(_translate("MainWindow", "Born in 2001"))
        self.pushButtontop3.setText(_translate("MainWindow", "Top 3 oldest "))
        self.pushButtonrole.setText(_translate("MainWindow", " Tester role "))
        self.pushButtoncount.setText(_translate("MainWindow", "Count "))
