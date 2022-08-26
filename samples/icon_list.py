import pyqt5_fugueicons as fugue
import sys
from PyQt5 import QtCore, QtWidgets

def makeListWidget():
    l = QtWidgets.QListWidget()
    
    for i, name in enumerate(fugue.iconNames()):
        l.addItem(QtWidgets.QListWidgetItem(fugue.icon(name), str(i + 1) + ' - ' + name))

    return l

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    win.setWindowTitle('pyqt5_fugueicons - icon_list.py')
    win.setMinimumSize(QtCore.QSize(800, 600))
    win.setCentralWidget(makeListWidget())
    win.show()

    return app.exec()

if __name__ == '__main__':
    sys.exit(main())