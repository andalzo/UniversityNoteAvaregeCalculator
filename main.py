from source.main_window import MainWindow
from PySide2 import QtWidgets
import sys


def main():
    app0 = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app0.exec_())


if __name__ == '__main__':
    main()
