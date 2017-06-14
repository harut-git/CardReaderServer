import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import QObject, pyqtSlot, QIODevice, pyqtSignal
from PyQt5.QtSerialPort import QSerialPort

PORT = 'COM59'


class DVIFlasher(QObject):
    ser = None
    flash_done = pyqtSignal(int, int)

    def __init__(self):
        super(DVIFlasher, self).__init__()
        self.ser = QSerialPort(PORT)
        self.ser.readyRead.connect(self.read)

    def flash(self):
        print(self.ser.open(QIODevice.ReadWrite))
        self.ser.setBaudRate(115200)

    def read(self):
        print("Got data")
        self.ser.close()
        self.flash_done.emit(0, 0)


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.btn = QPushButton("Start", self)
        self.flasher = DVIFlasher()
        self.btn.clicked.connect(self.flasher.flash)
        self.resize(self.btn.sizeHint())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Widget()
    win.show()
    sys.exit(app.exec_())