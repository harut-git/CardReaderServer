# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import sys
from PyQt4.QtGui import QApplication

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


class MainWindow(QtGui.QMainWindow):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("MainWindow"))
        main_window.resize(800, 600)
        main_window.setMinimumSize(QtCore.QSize(800, 600))
        main_window.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtGui.QWidget(main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        main_window.setCentralWidget(self.centralwidget)
        self.emp_pic = QtGui.QLabel(self.centralwidget)
        self.emp_pic.setGeometry(QtCore.QRect(570, 10, 141, 121))
        self.emp_pic.setText(_fromUtf8(""))
        self.emp_pic.setPixmap(QtGui.QPixmap(_fromUtf8("../../Pictures/user.png")))
        self.emp_pic.setScaledContents(True)
        self.emp_pic.setObjectName(_fromUtf8("label"))
        self.emp_list = QtGui.QListView(self.centralwidget)
        self.emp_list.setGeometry(QtCore.QRect(50, 30, 331, 521))
        self.emp_list.setObjectName(_fromUtf8("listView"))
        self.name = QtGui.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(550, 180, 201, 31))
        self.name.setObjectName(_fromUtf8("textEdit"))
        self.name.setPlaceholderText("name")
        self.surname = QtGui.QLineEdit(self.centralwidget)
        self.surname.setGeometry(QtCore.QRect(550, 230, 201, 31))
        self.surname.setObjectName(_fromUtf8("textEdit_2"))
        self.surname.setPlaceholderText("surname")
        self.group = QtGui.QLineEdit(self.centralwidget)
        self.group.setGeometry(QtCore.QRect(550, 280, 201, 31))
        self.group.setObjectName(_fromUtf8("textEdit_3"))
        self.group.setPlaceholderText("group")
        self.position = QtGui.QLineEdit(self.centralwidget)
        self.position.setGeometry(QtCore.QRect(550, 330, 201, 31))
        self.position.setObjectName(_fromUtf8("textEdit_4"))
        self.position.setPlaceholderText("position")
        self.start_time = QtGui.QLineEdit(self.centralwidget)
        self.start_time.setGeometry(QtCore.QRect(550, 380, 201, 31))
        self.start_time.setObjectName(_fromUtf8("textEdit_5"))
        self.start_time.setPlaceholderText("start time")
        self.end_time = QtGui.QLineEdit(self.centralwidget)
        self.end_time.setGeometry(QtCore.QRect(550, 430, 201, 31))
        self.end_time.setObjectName(_fromUtf8("textEdit_6"))
        self.end_time.setPlaceholderText("end time")
        self.comment = QtGui.QLineEdit(self.centralwidget)
        self.comment.setGeometry(QtCore.QRect(550, 480, 201, 31))
        self.comment.setObjectName(_fromUtf8("textEdit_7"))
        self.comment.setPlaceholderText("comment")
        self.save_button = QtGui.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(540, 520, 99, 27))
        self.save_button.setObjectName(_fromUtf8("pushButton"))
        self.cancel_button = QtGui.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(660, 520, 99, 27))
        self.cancel_button.setObjectName(_fromUtf8("pushButton_2"))
        self.menubar = QtGui.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(main_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        main_window.setStatusBar(self.statusbar)
        self.retranslateUi(main_window)
        QtCore.QObject.connect(self.save_button, QtCore.SIGNAL("clicked()"), self.pushButtonClicked)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.save_button.setText(_translate("MainWindow", "Save", None))
        self.cancel_button.setText(_translate("MainWindow", "Cancel", None))

    def pushButtonClicked(self):
        dialog = Ui_Dialog()
        dialog.setupUi(dialog)
        dialog.show()
        dialog.exec_()

    def send(self, word):
        print word


class Ui_Dialog(QtGui.QDialog):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("Dialog"))
        dialog.resize(540, 400)
        dialog.setMinimumSize(540, 400)
        dialog.setMaximumSize(540, 400)
        self.buttonBox = QtGui.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label = QtGui.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(300, 20, 200, 200))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../../Pictures/user.png")))
        self.label.setScaledContents(True)

        btn = QtGui.QPushButton('Browse', dialog)
        btn.resize(btn.sizeHint())
        btn.move(360, 250)
        QtCore.QObject.connect(btn, QtCore.SIGNAL("clicked()"), self.SingleBrowse)
        self.textEdit_7 = QtGui.QLineEdit(dialog)
        self.textEdit_7.setGeometry(QtCore.QRect(40, 320, 201, 31))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.textEdit_3 = QtGui.QLineEdit(dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 120, 201, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_5 = QtGui.QLineEdit(dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(40, 220, 201, 31))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_6 = QtGui.QLineEdit(dialog)
        self.textEdit_6.setGeometry(QtCore.QRect(40, 270, 201, 31))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.textEdit = QtGui.QLineEdit(dialog)
        self.textEdit.setGeometry(QtCore.QRect(40, 20, 201, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QLineEdit(dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(40, 70, 201, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_4 = QtGui.QLineEdit(dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(40, 170, 201, 31))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))

    def SingleBrowse(self):
        file_path = QtGui.QFileDialog.getOpenFileName(QtGui.QFileDialog(),
                                                     'Single File',
                                                     "~/Desktop/PyRevolution/PyQt4",
                                                     '*.txt')
        print('filePath', file_path, '\n')

        file_handle = open(file_path, 'r')
        lines = file_handle.readlines()
        for line in lines:
            print(line)


class MainDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.textEdit_2 = QtGui.QLineEdit(self)
        self.textEdit_2.setGeometry(QtCore.QRect(550, 230, 201, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QLineEdit(self)
        self.textEdit_3.setGeometry(QtCore.QRect(550, 280, 201, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_4 = QtGui.QLineEdit(self)
        self.textEdit_4.setGeometry(QtCore.QRect(550, 330, 201, 31))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.textEdit_5 = QtGui.QLineEdit(self)
        self.textEdit_5.setGeometry(QtCore.QRect(550, 380, 201, 31))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_6 = QtGui.QLineEdit(self)
        self.textEdit_6.setGeometry(QtCore.QRect(550, 430, 201, 31))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.textEdit_7 = QtGui.QLineEdit(self)
        self.textEdit_7.setGeometry(QtCore.QRect(550, 480, 201, 31))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(550, 520, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 520, 99, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.setupUi(myapp)
    myapp.show()
    sys.exit(app.exec_())
