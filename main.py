from PyQt4 import QtCore, QtGui, uic

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		uic.loadUi("mainwindow.ui", self)
		self.addButton.clicked.connect(self.addButtonClicked)
		self.subviewsLayout.setAlignment(QtCore.Qt.AlignTop)


	def addButtonClicked(self):
		b = SubView()
		self.subviewsLayout.insertWidget(0, b)


class SubView(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		uic.loadUi("subview.ui", self)
		self.pushButton.clicked.connect(self.buttonClicked)

	def buttonClicked(self):
		self.lineEdit.setText('clicked!')


if __name__ == '__main__':
	import sys
	app = QtGui.QApplication(sys.argv)
	mw = MainWindow()
	mw.show()
	app.exec_()
