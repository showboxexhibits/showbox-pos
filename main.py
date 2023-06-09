#!/usr/bin/python3

'''
    Welcome to the main initialization of the point-of-sale register UI by Showbox Exhibits

    This file is intended to be run at boot and used as the primary (only) means of
    end-user interaction with the machine. This GUI has been designed for use with
    a touchscreen interface, rather than a standard keyboard.
'''

# These import statements pull from all other associated scripts with this application.
# It also pulls from the fantastic PyQt5 and  python-barcode libraries.
import os
from PyQt5 import QtGui, QtWidgets
#from QtCore import Qt
from QtGui import QPixmap, QBrush, QPalette
from QtWidgets import QPushButton, QMainWindow, QApplication

# This is the initialization of the main window of the application.
# This window serves as the tray in which other windows and widgets are placed.

# I have created many syntax errors with the new import statements, fix this demo.
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        script_dir = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(
            script_dir,
            "assets/main-screen/main-screen.png"
        )

        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio)

        palette = QPalette()
        palette.setBrush(QPalette.Background), QBrush(scaled_pixmap)

        self.setPalette(palette)
        # This is all code for testing purposes, it and this comment will be removed.

        self.setGeometry(0, 0, 1920, 1080)

        self.button = QPushButton('Button', self)
        self.button.move(60, 50)

        self.button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        print("Button output")

# The QApplication class opens up the use of PyQt5 signals for the GUI.
# PyQt5 applications only need one single instance of QApplication.
app = QApplication([])

# Assigning the MainWindow to a variable and calling .show() draws the window on screen.
window = MainWindow()
window.show()

# Finally, after all assignments have been made, the app is executed.
app.exec_()
