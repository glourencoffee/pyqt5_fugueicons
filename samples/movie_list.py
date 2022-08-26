import pyqt5_fugueicons as fugue
import sys
from PyQt5 import QtCore, QtWidgets

def makeCentralWidget():
    l = QtWidgets.QGridLayout()
    l.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

    for row, name in enumerate(fugue.movieNames()):
        name_label = QtWidgets.QLabel(str(row + 1) + ' - ' + name)

        movie = fugue.movie(name)
        movie.start()

        # Repeat 'counter' movies because they stop animating
        # when counting reaches a certain value.
        movie.finished.connect(movie.start)
        movie_label = QtWidgets.QLabel()
        movie_label.setMovie(movie)
        
        l.addWidget(name_label,  row, 0)
        l.addWidget(movie_label, row, 1)

    w = QtWidgets.QWidget()
    w.setLayout(l)

    return w

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    win.setWindowTitle('pyqt5_fugueicons - movie_list.py')
    win.setMinimumSize(QtCore.QSize(600, 400))
    win.setCentralWidget(makeCentralWidget())
    win.show()

    return app.exec()

if __name__ == '__main__':
    sys.exit(main())