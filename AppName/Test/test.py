from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtCore import QObject, pyqtSignal, QThread
from PyQt5.QtWidgets import *
import sys

base, form = uic.loadUiType('gui.ui')  # The base class is QDialog, QWidget or QMainWindow

class MainWindow(base, form):

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec_())