import sys
from PyQt4.QtGui import QApplication
from PLGui import PyLonGui

if __name__=="__main__":

	app = QApplication(sys.argv)
	pylon_win = PyLonGui()
	pylon_win.show()
	sys.exit(app.exec_())
