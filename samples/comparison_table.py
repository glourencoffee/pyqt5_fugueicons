import pyqt5_fugueicons as fugue
import sys
from PyQt5 import QtCore, QtWidgets

def makeTableWidget():
    headers = (
        'Filename',
        '16x16',
        '16x16, shadowless',
        '24x24',
        '24x24, shadowless',
        '32x32',
        '32x32, shadowless',
        'Gif'
    )

    icon_names = fugue.iconNames()[:100]

    table = QtWidgets.QTableWidget()
    table.setEditTriggers(table.EditTrigger.NoEditTriggers)
    table.setRowCount(len(icon_names))
    table.setColumnCount(len(headers))
    table.setHorizontalHeaderLabels(headers)

    movie_column = table.columnCount() - 1

    for row, name in enumerate(icon_names):
        table.setItem(row, 0, QtWidgets.QTableWidgetItem(name))

        for i, size in enumerate((16, 24, 32)):
            shadowed_icon   = fugue.icon(name, shadowless=False, size=size)
            shadowless_icon = fugue.icon(name, shadowless=True,  size=size)

            table.setItem(row, (i * 2) + 1, QtWidgets.QTableWidgetItem(shadowed_icon,   ''))
            table.setItem(row, (i * 2) + 2, QtWidgets.QTableWidgetItem(shadowless_icon, ''))

        movie = fugue.movie(name)
        label = QtWidgets.QLabel()

        if movie.isValid():
            movie.start()
            movie.finished.connect(movie.start)
            label.setMovie(movie)
        else:
            label.setText('N/A')

        table.setItem(row, movie_column, QtWidgets.QTableWidgetItem())
        table.setCellWidget(row, movie_column, label)

    table.resizeColumnsToContents()
    table.setIconSize(QtCore.QSize(32, 32))

    return table

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    win.setWindowTitle('pyqt5_fugueicons - comparison_table.py')
    win.setMinimumSize(QtCore.QSize(800, 600))
    win.setCentralWidget(makeTableWidget())
    win.show()

    return app.exec()

if __name__ == '__main__':
    sys.exit(main())