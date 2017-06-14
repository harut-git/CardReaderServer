from PyQt5 import QtCore, QtGui, QtWidgets
# from DbConnect import db_conn
import sys
from PyQt5.QtCore import pyqtSlot
from shutil import copyfile

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(800, 640)
        main_window.setMinimumSize(QtCore.QSize(800, 640))
        main_window.setMaximumSize(QtCore.QSize(800, 640))
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        main_window.setCentralWidget(self.centralwidget)
        self.emp_pic = QtWidgets.QLabel(self.centralwidget)
        self.emp_pic.setGeometry(QtCore.QRect(575, 20, 150, 150))
        self.emp_pic.setText("")
        self.emp_pic.setPixmap(QtGui.QPixmap("../../Pictures/user.png"))
        self.emp_pic.setScaledContents(True)
        self.emp_pic.setObjectName("label")
        self.emp_list = QtWidgets.QListView(self.centralwidget)
        self.emp_list.setGeometry(QtCore.QRect(50, 20, 400, 580))
        self.emp_list.setObjectName("listView")
        self.entry_id = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_id.setGeometry(QtCore.QRect(550, 180, 201, 31))
        self.entry_id.setObjectName("textEdit")
        self.entry_id.setPlaceholderText("entry id")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(550, 230, 201, 31))
        self.name.setObjectName("textEdit")
        self.name.setPlaceholderText("name")
        self.surname = QtWidgets.QLineEdit(self.centralwidget)
        self.surname.setGeometry(QtCore.QRect(550, 280, 201, 31))
        self.surname.setObjectName("textEdit_2")
        self.surname.setPlaceholderText("surname")
        self.group = QtWidgets.QLineEdit(self.centralwidget)
        self.group.setGeometry(QtCore.QRect(550, 330, 201, 31))
        self.group.setObjectName("textEdit_3")
        self.group.setPlaceholderText("group")
        self.position = QtWidgets.QLineEdit(self.centralwidget)
        self.position.setGeometry(QtCore.QRect(550, 380, 201, 31))
        self.position.setObjectName("textEdit_4")
        self.position.setPlaceholderText("position")
        self.start_time = QtWidgets.QLineEdit(self.centralwidget)
        self.start_time.setGeometry(QtCore.QRect(550, 430, 201, 31))
        self.start_time.setObjectName("textEdit_5")
        self.start_time.setPlaceholderText("start time")
        self.end_time = QtWidgets.QLineEdit(self.centralwidget)
        self.end_time.setGeometry(QtCore.QRect(550, 480, 201, 31))
        self.end_time.setObjectName("textEdit_6")
        self.end_time.setPlaceholderText("end time")
        self.comment = QtWidgets.QLineEdit(self.centralwidget)
        self.comment.setGeometry(QtCore.QRect(550, 530, 201, 31))
        self.comment.setObjectName("textEdit_7")
        self.comment.setPlaceholderText("comment")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(540, 580, 99, 27))
        self.save_button.setObjectName("pushButton")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(660, 580, 99, 27))
        self.cancel_button.setObjectName("pushButton_2")
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.retranslateUi(main_window)
        self.save_button.clicked.connect(self.pushButtonClicked)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.save_button.setText(_translate("MainWindow", "Save", None))
        self.cancel_button.setText(_translate("MainWindow", "Cancel", None))

    @pyqtSlot(name='pushbuttonclicked')
    def pushButtonClicked(self):
        dialog = MainDialog()
        dialog.setupUi(dialog)
        dialog.show()
        dialog.exec_()


class MainDialog(QtWidgets.QDialog):
    def setupUi(self, dialog):
        dialog.setObjectName("Dialog")
        dialog.resize(540, 420)
        dialog.setMinimumSize(540, 420)
        dialog.setMaximumSize(540, 420)
        self.save_button = QtWidgets.QPushButton(dialog)
        self.save_button.setGeometry(QtCore.QRect(300, 370, 99, 27))
        self.save_button.setObjectName("pushButton")
        self.save_button.setText("Save")
        self.cancel_button = QtWidgets.QPushButton(dialog)
        self.cancel_button.setGeometry(QtCore.QRect(410, 370, 99, 27))
        self.cancel_button.setObjectName("pushButton_2")
        self.cancel_button.setText("Cancel")
        self.emp_pic = QtWidgets.QLabel(dialog)
        self.emp_pic.setGeometry(QtCore.QRect(300, 20, 200, 200))
        self.emp_pic.setText((""))
        self.emp_pic.setPixmap(QtGui.QPixmap("../../Pictures/user.png"))
        self.emp_pic.setScaledContents(True)

        browse = QtWidgets.QPushButton('Browse', dialog)
        browse.resize(browse.sizeHint())
        browse.move(360, 250)
        self.entry_id = QtWidgets.QLineEdit(dialog)
        self.entry_id.setGeometry(QtCore.QRect(40, 20, 201, 31))
        self.entry_id.setObjectName("textEdit")
        self.entry_id.setPlaceholderText("entry id")
        self.name = QtWidgets.QLineEdit(dialog)
        self.name.setGeometry(QtCore.QRect(40, 70, 201, 31))
        self.name.setObjectName("textEdit")
        self.name.setPlaceholderText("name")
        self.surname = QtWidgets.QLineEdit(dialog)
        self.surname.setGeometry(QtCore.QRect(40, 120, 201, 31))
        self.surname.setObjectName("textEdit_2")
        self.surname.setPlaceholderText("surname")
        self.group = QtWidgets.QLineEdit(dialog)
        self.group.setGeometry(QtCore.QRect(40, 170, 201, 31))
        self.group.setObjectName("textEdit_3")
        self.group.setPlaceholderText("group")
        self.position = QtWidgets.QLineEdit(dialog)
        self.position.setGeometry(QtCore.QRect(40, 220, 201, 31))
        self.position.setObjectName("textEdit_4")
        self.position.setPlaceholderText("position")
        self.start_time = QtWidgets.QLineEdit(dialog)
        self.start_time.setGeometry(QtCore.QRect(40, 270, 201, 31))
        self.start_time.setObjectName("textEdit_5")
        self.start_time.setPlaceholderText("start time")
        self.end_time = QtWidgets.QLineEdit(dialog)
        self.end_time.setGeometry(QtCore.QRect(40, 320, 201, 31))
        self.end_time.setObjectName("textEdit_6")
        self.end_time.setPlaceholderText("end time")
        self.comment = QtWidgets.QLineEdit(dialog)
        self.comment.setGeometry(QtCore.QRect(40, 370, 201, 31))
        self.comment.setObjectName("textEdit_7")
        self.comment.setPlaceholderText("comment")
        browse.clicked.connect(self.SingleBrowse)
        self.save_button.clicked.connect(self.save)

    @pyqtSlot(name="save")
    def save(self):
        new_url = "images/" + self.entry_id.text() + '.jpg'
        copyfile(self.file_path[0], new_url)

                # try:
                #     con = db_conn()
                #     con.set_character_set('utf8')
                #     cur = con.cursor()
                #     cur.execute(
                #         "INSERT INTO employees VALUES (NULL, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
                #             new_url,
                #             self.entry_id.text(),
                #             self.name.text(),
                #             self.sur_name.text(),
                #             self.position.text(),
                #             self.group.text(),
                #             self.start_time.text(),
                #             self.end_time.text(),
                #             self.comment.text()))
                # except Exception as e:
                #     print(e)

    @pyqtSlot(name='browse')
    def SingleBrowse(self):
        self.file_path = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QFileDialog(), filter='*.jpg')
        print(self.file_path[0])
        self.emp_pic.setPixmap(QtGui.QPixmap(self.file_path[0]))
        print(self.file_path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.setupUi(myapp)
    myapp.show()
    sys.exit(app.exec_())
