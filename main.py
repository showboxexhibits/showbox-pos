#!/usr/bin/python3

'''
    Welcome to the main initialization of the point-of-sale register UI by Showbox Exhibits

    This file is intended to be run at boot and used as the primary (only) means of
    end-user interaction with the machine. This GUI has been designed for use with
    a touchscreen interface, rather than a standard keyboard.
'''
import sys
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QInputDialog, QLineEdit
from libs.buttons.button import make_button

def init_buttons(self):
    self.deleteLastButton = make_button(self, "deleteLast")
    self.deleteLastButton.clicked.connect(self.delete_last)
    self.clearAllButton = make_button(self, "clearAll")
    self.clearAllButton.clicked.connect(self.clear_all)
    self.checkOutButton = make_button(self, "checkOut")
    self.checkOutButton.clicked.connect(self.check_out)
    self.closeButton = make_button(self, "close")
    self.closeButton.clicked.connect(self.close_app)

def init_labels(self):
    pass


with open("data.json", "rb") as raw_data:
    data = json.load(raw_data)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.lineEdit = QLineEdit()
        self.lineEdit.setDisabled(False)
        self.lineEdit.setText('')
        self.lineEdit.setEchoMode(1)
        self.startNew=1

        # Window exclusive stuff
        self.setAnimated(True)
        self.setObjectName('MainWindow')
        stylesheet = """
    #MainWindow{
        background-image: url(assets/main-screen/main-screen.png);
        background-repeat: no-repeat;
        background-position: center;
    }
        """

        self.setStyleSheet(stylesheet)

        init_buttons(self)
        self.itemNamePane = QtWidgets.QLabel()
        self.itemNamePane.setText("")
        self.itemNamePane.move(200, 200)
        self.itemNamePane.resize(300, 100)

        self.lineEdit.returnPressed.connect(self.scan_item)
        self.lineEdit.textChanged.connect(self.clear_input)

    def scan_item(self):
        scannerInput = self.lineEdit.text()
        barcode = ''.join(char for char in scannerInput if char.isdigit())
        if barcode in data:
            self.itemNamePane.setText((data[barcode]['name']).upper())
            print(data[barcode]['name'])
            self.startNew=1
        else:
            self.itemNamePane.setText("Unrecognized Item")

    def clear_input(self, text):
        if self.startNew:
            self.lineEdit.setText(text[-1])
            self.startNew=0

    def delete_last(self):
        print("Deleted last")
        self.deleteLastButton.setText("Yeet")

    def clear_all(self):
        print("Cleared all")
        self.clearAllButton.setText("Sweet!")

    def check_out(self):
        print("Checked out")
        self.checkOutButton.setText("All donezo")

    def close_app(self):
        sys.exit()


app = QApplication([])

# Assigning the MainWindow to a variable and calling .show() draws the window on screen.
window = MainWindow()
window.setGeometry(0,0,800,800)
window.showFullScreen()
window.show()

# Finally, after all assignments have been made, the app is executed.
app.exec_()
