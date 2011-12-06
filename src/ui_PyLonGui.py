# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/PyLonGui.ui'
#
# Created: Sun Aug 21 01:57:05 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QHBoxLayout, QGridLayout, QVBoxLayout
from PLTE import MyTextEdit,  MyHighlighter
from buildin_diction import Diction
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QCompleter

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.x_size = 800
        self.y_size = 600
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(self.x_size, self.y_size)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutgrid = QGridLayout()
        self.layouthorizontal = QHBoxLayout()
        self.layouthorizontal1 = QHBoxLayout()
        self.layoutgrid.addItem(self.layouthorizontal, 0, 0)
        self.layoutgrid.addItem(self.layouthorizontal1, 1, 0)
        
        self.sizeHi = MainWindow.sizeHint()
        print(self.sizeHi)
        self.NewButton = QtGui.QPushButton(self.centralwidget)
        self.NewButton.setGeometry(QtCore.QRect(10, 10, 99, 23))
        self.NewButton.setObjectName(_fromUtf8("NewButton"))
        self.SaveButton = QtGui.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(120, 10, 99, 23))
        self.SaveButton.setObjectName(_fromUtf8("SaveButton"))
        self.SaveAsButton = QtGui.QPushButton(self.centralwidget)
        self.SaveAsButton.setGeometry(QtCore.QRect(340, 10, 99, 23))
        self.SaveAsButton.setObjectName(_fromUtf8("SaveAsButton"))
        self.LoadButton = QtGui.QPushButton(self.centralwidget)
        self.LoadButton.setGeometry(QtCore.QRect(230, 10, 99, 23))
        self.LoadButton.setObjectName(_fromUtf8("LoadButton"))
#        self.LoadButton.set
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 850, 700))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.layouthorizontal.addWidget(self.NewButton, Qt.AlignLeft)
        self.layouthorizontal.addWidget(self.SaveButton, Qt.AlignLeft)
        self.layouthorizontal.addWidget(self.SaveAsButton, Qt.AlignLeft)
        self.layouthorizontal.addWidget(self.LoadButton, Qt.AlignLeft)
        self.layouthorizontal1.addWidget(self.scrollArea)
        #self.scrollAreaWidgetContents = QtGui.QWidget()
        #self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1580, 1190))
        #self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        
        self.words = Diction().RetDictBuild()
        self.words = self.words + Diction().RetDictDefClass()
        self.completer = QCompleter(self.words)
        #self.completer.setCaseSensitivity(Qt.CaseSensitive)
        #self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.textEdit = MyTextEdit(self.scrollArea)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setTabStopWidth(20)
        self.textEdit.setCompleter(self.completer)
        #self.layout.addWidget(self.textEdit)

#        self.textEdit.setWidget(self.scrollArea)

        highlighter = MyHighlighter(self.textEdit.document())
        self.scrollArea.setWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.centralwidget.setLayout(self.layoutgrid)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.NewButton.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveButton.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadButton.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveAsButton.setText(QtGui.QApplication.translate("MainWindow", "Save As", None, QtGui.QApplication.UnicodeUTF8))

