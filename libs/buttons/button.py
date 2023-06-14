import sys
from PyQt5 import QtWidgets

def make_button(window, name):
    if name == "deleteLast":
        b = QtWidgets.QPushButton(window)
        b.setText("Delete Last")
        b.move(825, 610)
        b.resize(298, 77)
        b.setFlat(True)
        return b
    if name == "clearAll":
        b = QtWidgets.QPushButton(window)
        b.setText("Clear All")
        b.move(1153, 609)
        b.resize(298, 77)
        b.setFlat(True)
        return b
    if name == "close":
        b = QtWidgets.QPushButton(window)
        b.setText("Close")
        b.move(400,400)
        b.resize(500,500)
        return b
    if name == "checkOut":
        b = QtWidgets.QPushButton(window)
        b.setText("Checkout")
        b.move(1445, 789)
        b.resize(376, 186)
        b.setFlat(True)
        return b
    else:
        return "error"
