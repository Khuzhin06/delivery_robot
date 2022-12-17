import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from delivery_robot.v2 import design
from port import serial_ports, speeds
import serial


class LedApp(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Port.addItems(serial_ports())
        self.Speed.addItems(speeds)
        self.realport = None
        self.connect.pressed.connect(self.connect_)
        # self.EnableBtn.clicked.connect(self.send)

    def connect_(self):
        try:
            self.realport = serial.Serial(self.Port.currentText(), int(self.Speed.currentText()))
            self.ConnectButton.setStyleSheet("background-color: green")
            self.ConnectButton.setText('Подключено')
        except Exception as e:
            print(e)

    def send(self):
        if self.realport:
            self.realport.write(b'1')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LedApp()
    window.show()
    app.exec_()
