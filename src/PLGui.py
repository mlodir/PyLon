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
            self.autoSelf = False
            self.indentSelf = 0
            self.quoteS = False
    
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
    
    def disconnectCursor(self):
        self.disconnect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
    
    def connectCursor(self):
        self.connect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
    
    def getInfo(self):
        if(not self.textEdit.getIndentNow()):
            self.textEdit.needNextIndent()
            self.textEdit.setCurrentIndent(self.currentIndent())
            
        if self.textEdit.getIndentNow():
            self.disconnectCursor()
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
            self.connectCursor()
            
        if self.textEdit.getParenthesis():
            self.disconnectCursor()
            self.autoParenthesis()
            self.connectCursor()
        
        if self.textEdit.getQuote():
            self.disconnectCursor()
            self.autoQuote()
            self.connectCursor()
        
        if self.textEdit.getQuoteS():
            self.disconnectCursor()
            self.autoQuoteS()
            self.connectCursor()
            
        if self.textEdit.getBracket():
            self.disconnectCursor()
            self.autoBracket()
            self.connectCursor()
            
        if self.textEdit.getBrace():
            self.disconnect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
            self.autoBrace()
            self.connect(self.textEdit, SIGNAL("cursorPositionChanged()"), self.getInfo)
        
        if self.textEdit.getComma():
            self.disconnect(self.textEdit,  SIGNAL("cursorPositionChanged()"), self.getInfo)
            self.autoComma()
            self.connect(self.textEdit,  SIGNAL("cursorPositionChanged()"), self.getInfo)

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
        if (re.search("class", selected)):
            self.textEdit.insertPlainText("):")
            indent = self.currentIndent()
            self.setAutoSelf(True, indent+1)
            move = 2
        elif (re.search("def", selected)):
            idt = self.currentIndent()
            if self.getAutoSelf(idt):
                self.textEdit.insertPlainText("self):")
            else:
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
    
    def autoQuoteS(self):
        self.textEdit.insertPlainText("\'")
        self.textEdit.moveCursor(QTextCursor.Left, QTextCursor.MoveAnchor)
        self.textEdit.setQuoteS()

    def autoBracket(self):
        self.textEdit.insertPlainText("]")
        self.textEdit.moveCursor(QTextCursor.Left, QTextCursor.MoveAnchor)
        self.textEdit.setBracket()    
    
    def autoBrace(self):
        self.textEdit.insertPlainText("}")
        self.textEdit.moveCursor(QTextCursor.Left, QTextCursor.MoveAnchor)
        self.textEdit.setBrace() 
    #def nextIndent(self, current_indent):
    
    def autoComma(self):
        self.textEdit.insertPlainText(" ")
        self.textEdit.setComma()

    def setAutoSelf(self, indent, autoSelf = False):
        self.autoSelf = autoSelf
        self.indentSelf = indent
    
    def getAutoSelf(self, indent):
        if (self.indentSelf == indent):
            return self.autoSelf
        else:
            return False
    
    def getIndentSelf(self):
        return self.indentSelf
