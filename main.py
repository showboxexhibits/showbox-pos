import sys
import json
import logging
import os
import datetime
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QBrush
from libs.buttons.button import make_button
from version import get_version

def touch(logpath):
    with open(logpath, 'w'):
        os.utime(logpath, None)


current_datetime = datetime.datetime.now()
logpath = f"logs/{current_datetime}.log"
touch(logpath)

logging.basicConfig(level=logging.DEBUG,
                    filename=logpath,
                    format='%(asctime)s :: %(levelname)s :: %(message)s'
                    )
version_number = get_version()
logging.info('--- Application boot ---\n\nMOTD: \n-----\n"Welcome to ShowBox Exhibits POS System"\n-----\n')
logging.info(f'Version number {version_number} loaded')

with open("data.json", "r") as f:
    data = json.load(f)
    

style = """
                color: black;
                background-color: white;
                border-style: solid;
                border-color: red;
                border-width: 5px;
                font-size: 72px;
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
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.itemData = []
        self.tableItems = []
        self.background = BackgroundImage(self)
        self.background.setGeometry(self.rect())

        self.barcodeInput = QtWidgets.QLineEdit(self)
        self.barcodeInput.setGeometry(10, 10, 200, 40)
        self.barcodeInput.returnPressed.connect(self.scan_item)

        self.itemScanned = QtWidgets.QLabel(self)
        self.itemScanned.setStyleSheet(style)
        self.itemScanned.setAlignment(Qt.AlignCenter)
        self.itemScanned.setGeometry(130, 810, 561, 141)

        self.itemScannedImage = QtWidgets.QLabel(self.background)
        self.itemScannedImage.setGeometry(300, 300, 200, 200)

        self.itemTable = QtWidgets.QTableView(self)
        self.itemTable.setGeometry(830, 130, 941, 461)
        self.itemTable.resizeColumnsToContents()
        self.itemTable.resizeRowsToContents()
        self.itemTableModel = QtGui.QStandardItemModel(self)
        self.itemTableModel.setHorizontalHeaderLabels(["Qty.", "Name", "Price"])
        self.itemTable.setModel(self.itemTableModel)

        self.init_buttons()

        self.background.lower()
        self.setCentralWidget(self.background)

    def set_font(self, index):
        font = QtGui.QFont()
        font.setPointSize(18)
        index.setFont(font)

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
        logging.debug(f'Recieved input: {self.barcodeInput.text()}')
        scannerInput = self.barcodeInput.text()
        barcode = ''.join(char for char in scannerInput if char.isdigit())
        logging.debug(f'Input modified from {scannerInput} -> {barcode}')
        if barcode in self.data:
            item_name = self.data[barcode]['name']
            path = self.data[barcode]['image_path']
            price = self.data[barcode]['price']
            logging.debug(f'Barcode scanned: {barcode} :: Item name: {item_name}')
            try:
                pixmap = QtGui.QPixmap(path)
                self.itemScannedImage.setPixmap(pixmap.scaled(700, 700, QtCore.Qt.KeepAspectRatio))
            except Exception:
                logging.warning(f'Image could not be found for {barcode} :: {item_name}')
                pass
            self.itemScanned.setText(item_name.upper())
            self.itemScanned.setStyleSheet(style)
            itemData = [str(1), str(item_name), str(price)]
            if self.item_exists(itemData):
                pass
            else:
                self.insert_row(itemData)
            logging.info(f'Successful scan flow achieved: {barcode} :: {item_name}')
        else:
            logging.warning(f'Unrecgonized barcode: "{barcode}"')
        self.barcodeInput.clear()

    def item_exists(self, itemData):
        for row in range(self.itemTableModel.rowCount()):
            index = self.itemTableModel.index(row, 1)
            if self.itemTableModel.data(index) == itemData[1]:
                old_qty_item = self.itemTableModel.item(row, column=0)
                old_price_item = self.itemTableModel.item(row, column=2)
                logging.debug(f"Old Quantity Item: {old_qty_item}")
                logging.debug(f"Old Price Item: {old_price_item}")
                old_qty = old_qty_item.data(Qt.DisplayRole)
                old_price = old_price_item.data(Qt.DisplayRole)
                logging.debug(f"Old Qty Data: {old_qty}")
                logging.debug(f"Old Price Data:{old_price}")
                new_qty = QtGui.QStandardItem(str(int(old_qty) + 1))
                self.set_font(new_qty)
                new_price = QtGui.QStandardItem(str(float(old_price) + float(itemData[2])))
                self.set_font(new_price)
                self.itemTableModel.setItem(row, 0, new_qty)
                self.itemTableModel.setItem(row, 2, new_price)
                logging.debug(f"Changed table values according to {itemData}")
                return True
        return False

    def insert_row(self, itemData):
        self.log_table_state()
        row = self.itemTableModel.rowCount()
        items = []
        self.itemTableModel.insertRow(row)
        for column, value in enumerate(itemData):
            item = QtGui.QStandardItem(str(value))
            item.setData(str(value), Qt.DisplayRole)
            self.set_font(item)
            self.itemTableModel.setItem(row, column, item)
            items.append(item)
        self.tableItems.append(items)
        logging.debug(f"Added to table: {itemData}")
        self.log_table_state()

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

    def log_table_state(self):
        for row, items in enumerate(self.tableItems):
            row_data = [item.data() for item in items]
            logging.debug(f"Row {row} data: {row_data}")


def main():
    app = QtWidgets.QApplication([])
    window = MainWindow(data)
    window.showFullScreen()
    window.show()

    app.exec_()

if __name__ == '__main__':
    main()
