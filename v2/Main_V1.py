import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from delivery_robot.v2 import design
from port import serial_ports, speeds
import serial
import sqlite3


class LedApp(QtWidgets.QMainWindow, design.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Port.addItems(serial_ports())
        self.Speed.addItems(speeds)
        self.realport = None
        self.connect.pressed.connect(self.connection)
        self.Right.stateChanged.connect(self.send)
        self.Left.stateChanged.connect(self.send)
        self.Front_2.stateChanged.connect(self.send)
        self.Back.stateChanged.connect(self.send)
        # self.sl = {self.Right: '', self.Back: '', self.Front_2: '', self.Left: ''}

    def connection(self):
        try:
            self.realport = serial.Serial(self.Port.currentText(), int(self.Speed.currentText()))
            self.ConnectButton.setStyleSheet("background-color: green")
            self.ConnectButton.setText('Подключено')
        except Exception as e:
            print(e)

    def send(self):
        if self.realport:
            if self.sender().isChecked():
                if self.sender() == self.Left:
                    self.realport.write(b'3')
                if self.sender() == self.Right:
                    self.realport.write(b'4')
                if self.sender() == self.Front_2:
                    self.realport.write(b'1')
                if self.sender() == self.Back:
                    self.realport.write(b'2')
                data = self.realport.readline().decode('ascii')
                print(data)
            else:
                self.realport.write(b'0')

    def base(self):
        self.con = sqlite3.connect("data_base.db")
        self.cur = self.con.cursor()
        way, b = self.cur.execute(
            "SELECT way, name FROM base WHERE name = 'prototip'").fetchall()[0]
        print(way)
        self.con.close()

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = LedApp()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
