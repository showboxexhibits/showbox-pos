import sys
import json

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPalette, QBrush
from libs.buttons.button import make_button

with open("data.json", "r") as f:
    data = json.load(f)

style = """
            QLabel {
                color: black;
                background-color: white;
                border-style: flat;
                font-size: 72px;
                text-align: center;
            }
        """

class BackgroundImage(QtWidgets.QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Pull image
        self.pixmap = QtGui.QPixmap('assets/main-screen/main-screen.png')
        self.setAutoFillBackground(True)

    def resizeEvent(self, event):
        # Resize background when window is altered
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(self.pixmap)
        palette.setBrush(QtGui.QPalette.Background, brush)
        self.setPalette(palette)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.background = BackgroundImage(self)
        self.background.setGeometry(self.rect())

        self.barcodeInput = QtWidgets.QLineEdit(self)
        self.barcodeInput.setGeometry(10, 10, 200, 40)
        self.barcodeInput.returnPressed.connect(self.scan_item)

        self.itemScanned = QtWidgets.QLabel(self)
        self.itemScanned.setText(' ')
        self.itemScanned.setGeometry(130, 810, 561, 141)
        self.itemScanned.setStyleSheet(style)

        self.itemScannedImage = QtWidgets.QLabel(self.background)
        self.itemScannedImage.setGeometry(300, 300, 200, 200)

        self.init_buttons()

        self.background.lower()
        self.setCentralWidget(self.background)

    def resizeEvent(self, event):
        self.background.setGeometry(self.rect())
        super().resizeEvent(event)

    def init_buttons(self):
        # Create button
        self.deleteLastButton = make_button(self, "deleteLast")
        self.clearAllButton   = make_button(self, "clearAll")
        self.checkOutButton   = make_button(self, "checkOut")
        self.closeButton      = make_button(self, "close")
        self.secretMenuButton = make_button(self, "secretMenu")

        # Map button function
        self.deleteLastButton.clicked.connect(self.delete_last)
        self.clearAllButton.clicked.connect(self.clear_all)
        self.checkOutButton.clicked.connect(self.check_out)
        self.closeButton.clicked.connect(self.close_app)
        self.secretMenuButton.clicked.connect(self.activate_secret_menu)

    def scan_item(self):
        scannerInput = self.barcodeInput.text()
        barcode = ''.join(char for char in scannerInput if char.isdigit())
        print(f"User entered: {barcode}")
        if barcode in data:
            print(data[barcode]['name'])
            self.itemScanned.setText((data[barcode]['name']).upper())
            self.itemScanned.setStyleSheet(style)
            pixmap = QtGui.QPixmap(data[barcode]['image_path'])
            print(data[barcode]['image_path'])
            self.itemScannedImage.setPixmap(pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio))
        else:
            print("Error. Item not registered.")
        self.barcodeInput.clear()

    def delete_last(self):
        pass

    def clear_all(self):
        pass

    def check_out(self):
        pass

    def close_app(self):
        sys.exit()

    def activate_secret_menu(self):
        pass

def main():
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.showFullScreen()
    window.show()

    app.exec_()

if __name__ == '__main__':
    main()
