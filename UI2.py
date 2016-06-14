# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatGUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 80, 331, 491))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.UserList = QtGui.QListWidget(self.frame_2)
        self.UserList.setGeometry(QtCore.QRect(10, 40, 311, 431))
        self.UserList.setObjectName(_fromUtf8("UserList"))
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.RetrieveLog_2 = QtGui.QPushButton(self.frame_2)
        self.RetrieveLog_2.setGeometry(QtCore.QRect(220, 10, 91, 21))
        self.RetrieveLog_2.setObjectName(_fromUtf8("RetrieveLog_2"))
        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(360, 80, 431, 491))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.RetrieveLog = QtGui.QPushButton(self.frame_3)
        self.RetrieveLog.setGeometry(QtCore.QRect(330, 440, 91, 31))
        self.RetrieveLog.setObjectName(_fromUtf8("RetrieveLog"))
        self.User_LogRetrieve = QtGui.QTextEdit(self.frame_3)
        self.User_LogRetrieve.setGeometry(QtCore.QRect(10, 440, 311, 31))
        self.User_LogRetrieve.setObjectName(_fromUtf8("User_LogRetrieve"))
        self.MessageLogs = QtGui.QPlainTextEdit(self.frame_3)
        self.MessageLogs.setGeometry(QtCore.QRect(10, 40, 411, 391))
        self.MessageLogs.setReadOnly(True)
        self.MessageLogs.setObjectName(_fromUtf8("MessageLogs"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 781, 61))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 21, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.IP = QtGui.QPlainTextEdit(self.frame)
        self.IP.setGeometry(QtCore.QRect(40, 10, 291, 31))
        self.IP.setReadOnly(True)
        self.IP.setObjectName(_fromUtf8("IP"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(350, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Roboto"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.User = QtGui.QPlainTextEdit(self.frame)
        self.User.setGeometry(QtCore.QRect(440, 10, 321, 31))
        self.User.setReadOnly(False)
        self.User.setObjectName(_fromUtf8("User"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #QtCore.QObject.connect(self.RetrieveLog_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.UserList.clear)
        #QtCore.QObject.connect(self.UserList, QtCore.SIGNAL(_fromUtf8("itemClicked(QListWidgetItem*)")), self.MessageLogs.clear)
        QtCore.QObject.connect(self.RetrieveLog, QtCore.SIGNAL(_fromUtf8("clicked()")), self.User_LogRetrieve.copy)
        QtCore.QObject.connect(self.RetrieveLog, QtCore.SIGNAL(_fromUtf8("clicked()")), self.MessageLogs.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Intranet Chat", None))
        self.label.setText(_translate("MainWindow", "Available Users", None))
        self.RetrieveLog_2.setText(_translate("MainWindow", "REFRESH", None))
        self.label_2.setText(_translate("MainWindow", "Chat Log", None))
        self.RetrieveLog.setText(_translate("MainWindow", "SEND", None))
        self.label_5.setText(_translate("MainWindow", "IP ", None))
        self.label_6.setText(_translate("MainWindow", "Username", None))

def main():
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()