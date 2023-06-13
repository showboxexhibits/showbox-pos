from PyQt5 import QtWidgets

def clear_all():
    print("Clicked Clear All")

def delete_last(window):
    print("Clicked Delete Last")

def make_button(window, name):
    if name == "deleteLast":
        b = QtWidgets.QPushButton(window)
        b.setText("Delete Last")
        b.move(50, 50)
        b.clicked.connect(delete_last)
        return b
    if name == "clearAll":
        b = QtWidgets.QPushButton(window)
        b.setText("Clear All")
        b.move(50, 20)
        b.clicked.connect(clear_all)
        return b
    else:
        return "error"
