from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

def on_button_clicked():
    print("Button clicked!")

def main():

    app = QApplication([])

    w = QMainWindow()
    b = QPushButton('Click me!', w)
    b.move(60, 50)
    w.setWindowTitle('Simple')

    b.clicked.connect(on_button_clicked)
    
    w.show()

    app.exec_()

if __name__ == '__main__':

    main()
