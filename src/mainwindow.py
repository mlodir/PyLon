from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from ui_PyLonGui import Ui_MainWindow
from buildin_diction import Diction

class PyLonGui(QMainWindow, Ui_MainWindow):
	def __init__(self, parent = None):
		QMainWindow.__init__(self, parent)
		self.setupUi(self)

		self.path = QString()

		self.connect(self.SaveButton, SIGNAL("clicked()"),self.saveAction)
	
	def saveAction(self):
		print "CLICKED"
		fileName = QFileDialog.getSaveFileName(self,self.tr("Save"),"/home/towdy",self.tr("Python sources (*.py)"))
		print fileName
		text = self.getSourceCode()
		self.saveAs(text,fileName)


	def getSourceCode(self):
		return self.textEdit.toPlainText()

	def saveAs(self, text, fileName):
		save_code = open(fileName,"a")
		save_code.write(text)
		save_code.close()

	#def HTML(self,txt):
	#	self.textEdit.setHtml(txt)


'''class MyTextEdit(QtGui.QTextEdit):
	def __init__(self, parent = None):
		super(MyTextEdit,self).__init__(parent)
		self.setMinimumWidth(400)

	def setColor(self):
		print 'colorized!'

	def textUnderCursor(self):
		txt = self.textCursor()
		txt.select(QtGui.QTextCursor.WordUnderCursor)
		str(txt).join("dupa")
		self.textEdit.HTML(txt)
		return txt.selectedText()

	def keyPressEvent(self,event):
		if event.key()==QtCore.Qt.Key_Space:
			currentWord = self.textUnderCursor()
			print currentWord
			self.setColor()
			self.d = Diction().RetDict()
			if currentWord in self.d:
				print "self colorized"

		isShortcut = (event.modifiers() == QtCore.Qt.ControlModifier)

		if (not isShortcut):
			QtGui.QTextEdit.keyPressEvent(self, event)
'''