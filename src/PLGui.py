from ui_PyLonGui import Ui_MainWindow
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtGui import *
import re


class PyLonGui(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
            QMainWindow.__init__(self, parent)
            self.setupUi(self)
            self.colon = False
            self.cursor = QCursor()
            self.indentLevel = 0
            self.indent = "\t"
    
            self.connect(self.SaveButton, SIGNAL("clicked()"),self.saveAction)
            self.connect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)

    def saveAction(self):
        print("CLICKED")
        fileName = QFileDialog.getSaveFileName(self,self.tr("Save"),"/home/towdy",self.tr("Python sources (*.py)"))
        print(fileName)
        text = self.getSourceCode()
        self.saveAs(text,fileName)


    def getSourceCode(self):
        
        return self.textEdit.toPlainText()

    def saveAs(self, text, fileName):
        save_code = open(fileName,"a")
        save_code.write(text)
        save_code.close()

    def idt(self):
        textEdit.indent()
    
    def getInfo(self):
        if(not self.textEdit.getIndentNow()):
            self.textEdit.needNextIndent()
            self.textEdit.setCurrentIndent(self.currentIndent())
            
        if self.textEdit.getIndentNow():
            self.disconnect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
            print("indenting in progress")
            curin = self.textEdit.getCurrentIndent()
            print("curindlvl = "+str(curin))
            if self.textEdit.getNeedNewIndent():
                curin = curin + 1
                print(str(curin))
            for idt in range(0, curin):
                print("wcielo " + str(idt))
                self.textEdit.insertPlainText("\t")
            print("indentNow False")
            self.textEdit.setIndentNow(False)
            self.connect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
            
        if self.textEdit.getParenthesis():
            self.disconnect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
            self.autoParenthesis()
            self.connect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
        
        if self.textEdit.getQuote():
            self.disconnect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
            self.autoQuote()
            self.connect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
            
        if self.textEdit.getBracket():
            self.disconnect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
            self.autoBracket()
            self.connect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
            
        if self.textEdit.getBrace():
            self.disconnect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
            self.autoBrace()
            self.connect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)

   #Returns indent level of line under cursor
    def currentIndent(self):
        indent = 0
        cur = self.textEdit.textCursor()
        cur.select(QTextCursor.LineUnderCursor)
        selected = cur.selectedText()
        for char in selected:
            if char == "\t":
                indent = indent + 1
                    
        return indent

    def autoParenthesis(self):
        move = 0
        cur = self.textEdit.textCursor()
        cur.select(QTextCursor.LineUnderCursor)
        selected = cur.selectedText()
        if (re.search("class", selected)) or (re.search("def", selected)):
            self.textEdit.insertPlainText("):")
            move = 2
        else:
            self.textEdit.insertPlainText(")")
            move = 1
        #cur = self.textEdit.textCursor()
        for i in range(0, move):
            self.textEdit.moveCursor(QTextCursor.Left, QTextCursor.MoveAnchor)
        #elf.textEdit.setCursor(cur)
        self.textEdit.setParenthesis(False)
    
    def autoQuote(self):
        self.textEdit.insertPlainText("\"")
        self.textEdit.moveCursor(QTextCursor.Left, QTextCursor.MoveAnchor)
        self.textEdit.setQuote()

    def autoBracket(self):
        self.textEdit.insertPlainText("]")
        self.textEdit.moveCursor(QTextCursor.Left, QTextCursor.MoveAnchor)
        self.textEdit.setBracket()    
    
    def autoBrace(self):
        self.textEdit.insertPlainText("}")
        self.textEdit.moveCursor(QTextCursor.Left, QTextCursor.MoveAnchor)
        self.textEdit.setBrace() 
    #def nextIndent(self, current_indent):

