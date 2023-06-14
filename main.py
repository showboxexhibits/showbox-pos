#!/usr/bin/python3

'''
    Welcome to the main initialization of the point-of-sale register UI by Showbox Exhibits

    This file is intended to be run at boot and used as the primary (only) means of
    end-user interaction with the machine. This GUI has been designed for use with
    a touchscreen interface, rather than a standard keyboard.
'''
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        checked = 0
        
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
