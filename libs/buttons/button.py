from PyQt5 import QtWidgets

def make_button(window, name):
    if name == "deleteLast":
        b = QtWidgets.QPushButton(window)
        b.setText("")
        b.move(825, 610)
        b.resize(298, 77)
        b.setFlat(True)
        return b
    if name == "clearAll":
        b = QtWidgets.QPushButton(window)
        b.setText("")
        b.move(1153, 609)
        b.resize(298, 77)
        b.setFlat(True)
        return b
    if name == "close":
        b = QtWidgets.QPushButton(window)
        b.setText("")
        b.move(0, 0)
        return b
    if name == "checkOut":
        b = QtWidgets.QPushButton(window)
        b.setText("")
        b.move(1445, 789)
        b.resize(376, 186)
        b.setFlat(True)
        return b
    if name == "settings":
        pass
    if name == "networkConfiguration":
        pass
    if name == "updateNow":
        pass
    if name == "logSend":
        pass
    if name == "secretMenu":
        b = QtWidgets.QPushButton(window)
        b.resize(50, 50)
        b.move(1870, 0)
        return b
    else:
        return "error"
