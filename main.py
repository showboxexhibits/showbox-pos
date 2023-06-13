#!/usr/bin/python3

'''
    Welcome to the main initialization of the point-of-sale register UI by Showbox Exhibits

    This file is intended to be run at boot and used as the primary (only) means of
    end-user interaction with the machine. This GUI has been designed for use with
    a touchscreen interface, rather than a standard keyboard.
'''

import os
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from libs.buttons.button import make_button

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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

        make_button(self, "deleteLast")
        make_button(self, "clearAll")
        b = QtWidgets.QPushButton(self)
        b.setText("Close")
        b.move(200,200)
        b.clicked.connect(close_app)

def close_app():
    sys.exit()

app = QApplication([])

# Assigning the MainWindow to a variable and calling .show() draws the window on screen.
window = MainWindow()
window.setGeometry(0,0,800,800)
window.showFullScreen()
window.show()

# Finally, after all assignments have been made, the app is executed.
app.exec_()
