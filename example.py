import sys
import serial
import re, itertools
import _winreg as winreg
from PyQt4 import QtCore, QtGui
from datalogger_gui import Ui_Form

global ser, num, serportnum, comports
comports = []


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.scan, QtCore.SIGNAL("clicked()"), self.enumerate_serial_ports)
        QtCore.QObject.connect(self.ui.connect, QtCore.SIGNAL("clicked()"), self.connect_to_port)
        QtCore.QObject.connect(self.ui.disconnect, QtCore.SIGNAL("clicked()"), self.disconnect_from_port)
        QtCore.QObject.connect(self.ui.comdropdown, QtCore.SIGNAL('activated(int)'), self.connect_to_port)
        # QtCore.QObject.connect(self.ui.comdropdown, QtCore.SIGNAL('activated(int)'),self.set_baudrate)

    def disconnect_from_port(self):
        ser.close()

    def enumerate_serial_ports(self):

        path = 'HARDWARE\\DEVICEMAP\\SERIALCOMM'
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
        except WindowsError:
            raise IterationError
        # self.ui.statustextEdit.append('ports')
        for i in itertools.count():
            try:
                val = winreg.EnumValue(key, i)
                self.ui.statustextEdit.append(str(val[1]))
                comports.append(str(val[1]))
            except EnvironmentError:
                break
        self.ui.comdropdown.addItems(comports)
        BAUDRATES = list()
        BAUDRATES = [50, 75, 110, 134, 150, 200, 300, 600, 1200, 1800, 2400, 4800,
                     9600, 19200, 38400, 57600, 115200]
        self.ui.bauddropdown.addItems(BAUDRATES)

    # def set_baudrate(self,baud):
    def connect_to_port(self, num):
        portno = comports(num)
        ser = serial.Serial(portno, 1200, timeout=0)
        self.ui.statustextEdit.append('connected')
        self.ui.statustextEdit.append(str(num))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())