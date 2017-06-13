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
        self.emp_pic.setGeometry(QtCore.QRect(570, 10, 160, 160))
        self.emp_pic.setText(_fromUtf8(""))
        self.emp_pic.setPixmap(QtGui.QPixmap(_fromUtf8("../../Pictures/user.png")))
        self.emp_pic.setScaledContents(True)
        self.emp_pic.setObjectName(_fromUtf8("label"))
        self.emp_list = QtGui.QListView(self.centralwidget)
        self.emp_list.setGeometry(QtCore.QRect(50, 20, 400, 535))
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
        dialog = MainDialog()
        dialog.setupUi(dialog)
        dialog.show()
        dialog.exec_()


class MainDialog(QtGui.QDialog):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("Dialog"))
        dialog.resize(540, 400)
        dialog.setMinimumSize(540, 400)
        dialog.setMaximumSize(540, 400)
        self.save_button = QtGui.QPushButton(dialog)
        self.save_button.setGeometry(QtCore.QRect(300, 350, 99, 27))
        self.save_button.setObjectName(_fromUtf8("pushButton"))
        self.save_button.setText("Save")
        self.cancel_button = QtGui.QPushButton(dialog)
        self.cancel_button.setGeometry(QtCore.QRect(410, 350, 99, 27))
        self.cancel_button.setObjectName(_fromUtf8("pushButton_2"))
        self.cancel_button.setText("Cancel")
        self.emp_pic = QtGui.QLabel(dialog)
        self.emp_pic.setGeometry(QtCore.QRect(300, 20, 200, 200))
        self.emp_pic.setText(_fromUtf8(""))
        self.emp_pic.setPixmap(QtGui.QPixmap(_fromUtf8("../../Pictures/user.png")))
        self.emp_pic.setScaledContents(True)

        browse = QtGui.QPushButton('Browse', dialog)
        browse.resize(browse.sizeHint())
        browse.move(360, 250)
        QtCore.QObject.connect(browse, QtCore.SIGNAL("clicked()"), self.SingleBrowse)
        self.name = QtGui.QLineEdit(dialog)
        self.name.setGeometry(QtCore.QRect(40, 20, 201, 31))
        self.name.setObjectName(_fromUtf8("textEdit"))
        self.name.setPlaceholderText("name")
        self.surname = QtGui.QLineEdit(dialog)
        self.surname.setGeometry(QtCore.QRect(40, 70, 201, 31))
        self.surname.setObjectName(_fromUtf8("textEdit_2"))
        self.surname.setPlaceholderText("surname")
        self.group = QtGui.QLineEdit(dialog)
        self.group.setGeometry(QtCore.QRect(40, 120, 201, 31))
        self.group.setObjectName(_fromUtf8("textEdit_3"))
        self.group.setPlaceholderText("group")
        self.position = QtGui.QLineEdit(dialog)
        self.position.setGeometry(QtCore.QRect(40, 170, 201, 31))
        self.position.setObjectName(_fromUtf8("textEdit_4"))
        self.position.setPlaceholderText("position")
        self.start_time = QtGui.QLineEdit(dialog)
        self.start_time.setGeometry(QtCore.QRect(40, 220, 201, 31))
        self.start_time.setObjectName(_fromUtf8("textEdit_5"))
        self.start_time.setPlaceholderText("start time")
        self.end_time = QtGui.QLineEdit(dialog)
        self.end_time.setGeometry(QtCore.QRect(40, 270, 201, 31))
        self.end_time.setObjectName(_fromUtf8("textEdit_6"))
        self.end_time.setPlaceholderText("end time")
        self.comment = QtGui.QLineEdit(dialog)
        self.comment.setGeometry(QtCore.QRect(40, 320, 201, 31))
        self.comment.setObjectName(_fromUtf8("textEdit_7"))
        self.comment.setPlaceholderText("comment")
    def SingleBrowse(self):

        file_path = QtGui.QFileDialog.getOpenFileName(QtGui.QFileDialog(),
                                                      'Single File',
                                                      "~/Desktop/PyRevolution/PyQt4",
                                                      '*.jpg')
        self.emp_pic.setPixmap(QtGui.QPixmap(file_path))
        print file_path
        # except Exception as e:
        #     print e.message


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.setupUi(myapp)
    myapp.show()
    sys.exit(app.exec_())
