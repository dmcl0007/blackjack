import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def startWindow():
    app = QApplication(sys.argv)
    window = QWidget()
    b = QLabel(window)
    b.setText("Hello World!")
    window.setGeometry(200,200,200,50)
    b.move(50,20)
    window.setWindowTitle("BlackJack")
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    startWindow()