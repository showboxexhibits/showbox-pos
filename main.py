#!/usr/bin/python3

'''
    Welcome to the main initialization of the point-of-sale register UI by Showbox Exhibits

    This file is intended to be run at boot and used as the primary (only) means of
    end-user interaction with the machine. This GUI has been designed for use with
    a touchscreen interface, rather than a standard keyboard.
'''

import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

def init_buttons():
    pass    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


app = QApplication([])

# Assigning the MainWindow to a variable and calling .show() draws the window on screen.
window = MainWindow()
window.show()

# Finally, after all assignments have been made, the app is executed.
app.exec_()
