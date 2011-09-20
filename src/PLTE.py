from PyQt4 import QtGui
from PyQt4 import QtCore
from buildin_diction import Diction
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtGui import QSyntaxHighlighter

_cursor = QTextCursor()

def setStyle(colorSyntax, style=''):
    color = QColor()
    color.setNamedColor(colorSyntax)

    charColor = QTextCharFormat()
    charColor.setForeground(color)
    
    if 'bold' in style:
        charColor.setFontWeight(QFont.Bold)
    
    if 'italic' in style:
        charColor.setFontWeight(QFont.Italic)
    return charColor

STYLES = {
        'buildin': setStyle('blue', 'bold'), 
        'loops': setStyle('red'),
        'defclass': setStyle('black', 'bold'), 
        'dcname': setStyle('darkBlue', 'bold'), 
        'numbers': setStyle('cyan'), 
        'math': setStyle('green', 'bold'), 
        'braces': setStyle('black', 'bold')
        }

class MyTextEdit(QtGui.QTextEdit):
    def __init__(self, parent = None):
        super(MyTextEdit,self).__init__(parent)
        self.setMinimumWidth(400)
        self.needNewIndent = False
        self.currentIndent = 0
        self.indentNow = False
        self.parenthesis = False
        self.quote = False
        self.bracket = False
        self.brace = False
        self.completer = None
        self.returnPressed = False
        self.comma = False
        
        #self.doc = QTextDocument(None)

    def setCompleter(self, completer):
        if self.completer:
            self.disconnect(self.completer, 0, self, 0)
        if not completer:
            return

        completer.setWidget(self)
        completer.setCompletionMode(QtGui.QCompleter.PopupCompletion)
        completer.setCaseSensitivity(QtCore.Qt.CaseSensitive)
        self.completer = completer
        self.connect(self.completer,
            QtCore.SIGNAL("activated(const QString&)"), self.insertCompletion)

    def insertCompletion(self, completion):
        print("in insert method: ", self.textUnderCursor())
        tc = self.textCursor()
        extra = (len(completion) -
            len(self.completer.completionPrefix()))
        tc.movePosition(QtGui.QTextCursor.Left)
        tc.movePosition(QtGui.QTextCursor.EndOfWord)
        tc.insertText(completion[(len(completion))-(extra):])
        self.setTextCursor(tc)
        print("after insert: ", self.textUnderCursor())

    def textUnderCursor(self):
        txt = self.textCursor()
        txt.select(QtGui.QTextCursor.LineUnderCursor)
        selected = txt.selectedText()
        return selected

    def focusInEvent(self, event):
        if self.completer:
            self.completer.setWidget(self)
        QtGui.QTextEdit.focusInEvent(self, event)

    def keyPressEvent(self,event):
        event.accept()
        if event.key()==QtCore.Qt.Key_Return:
            print("returnPressed")
            
            print("indentNow")
            self.indentNow = True
            
        elif event.key()==QtCore.Qt.Key_ParenLeft:
            self.setParenthesis(True)
            
        elif event.key()==QtCore.Qt.Key_QuoteDbl:
            self.setQuote(True)
            
        elif event.key()==QtCore.Qt.Key_BracketLeft:
            self.setBracket(True)
            
        elif event.key()==QtCore.Qt.Key_BraceLeft:
            self.setBrace(True)
        
        elif event.key()==QtCore.Qt.Key_Comma:
            self.setComma(True)

        if self.completer.popup().isVisible():
            if event.key() in (
            QtCore.Qt.Key_Enter,
            QtCore.Qt.Key_Return,
            QtCore.Qt.Key_Escape,
            QtCore.Qt.Key_Tab,
            QtCore.Qt.Key_Backtab):
                event.ignore()
                print("event off")
                return
        else:
            event.accept()
 
        isShortcut = (event.modifiers() == QtCore.Qt.ControlModifier and event.key() == Qt.Key_E)
        
        if not self.completer or not isShortcut:
            QtGui.QTextEdit.keyPressEvent(self, event)
        
        ctrlOrShift = event.modifiers() in (QtCore.Qt.ControlModifier ,
                QtCore.Qt.ShiftModifier)
        
        if ctrlOrShift and event.text() == None:
            # ctrl or shift key on it's own
            return
        
        hasModifier = ((event.modifiers() != QtCore.Qt.NoModifier) and
                        not ctrlOrShift)
        
        eow = "~!@#$%^&*()_+{}|:\"<>?,./;'[]\\-=" #end of word
        ## ctrl or shift key on it's own??

        len_ev = len(event.text())
        str_ev = event.text()
        #print(rfind(eow, str_ev[len_ev - 2][len_ev -1]))
        
        completionPrefix = self.textUnderCursor()
        completionPrefix = completionPrefix.split("\t", self.currentIndent)
        completionPrefix = "".join(["%s" % el for el in completionPrefix])

        print("after split: ", completionPrefix)
        
        
        if (not isShortcut and (hasModifier or not event.text() or
        len(completionPrefix) < 3) or (str_ev[len_ev - 1] in eow)):
            self.completer.popup().hide()
            
            return

        if (completionPrefix != self.completer.completionPrefix()):
            self.completer.setCompletionPrefix(completionPrefix)
            popup = self.completer.popup()
            popup.setCurrentIndex(
                self.completer.completionModel().index(0,0))

        print("just before popup")
        print(self.textUnderCursor())
        
        cr = self.cursorRect()
        cr.setWidth(self.completer.popup().sizeHintForColumn(0)
            + self.completer.popup().verticalScrollBar().sizeHint().width())
        self.completer.complete(cr) ## popup it up!
        
        print("after popup: ", self.textUnderCursor())
        
        
    
    #Returns true if we need indent in new line of code
    def needNextIndent(self):
        cur = self.textCursor()
        cur.select(QTextCursor.LineUnderCursor)
        selected = cur.selectedText()
        length = len(selected)
        if length > 0:
            selected = selected[length - 1]
        
        if (selected == ":") and (not self.getIndentNow()):
            print("needNewIndent")
            self.setNeedNewIndent(True)
        else:
            self.setNeedNewIndent(False)

    def setCurrentIndent(self, indent):
        self.currentIndent = indent
    
    def setNeedNewIndent(self,  need):
        self.needNewIndent = need
    
    def getIndentNow(self):
        return self.indentNow

    def setIndentNow(self, indent = False):
        self.indentNow = indent

    def getCurrentIndent(self):
        return self.currentIndent
    
    def getNeedNewIndent(self):
        return self.needNewIndent

    def setParenthesis(self, parenthesis=False):
        print("paren TRUE")
        self.parenthesis = parenthesis
    
    def getParenthesis(self):
        return self.parenthesis
    
    def setBracket(self, bracket = False):
        self.bracket = bracket
    
    def getBracket(self):
        return self.bracket
    
    def setBrace(self, brace = False):
        self.brace = brace
    
    def getBrace(self):
        return self.brace
    
    def setQuote(self, quote = False):
        self.quote = quote
    
    def getQuote(self):
        return self.quote
    
    def setComma(self,  comma = False):
        self.comma = comma
    
    def getComma(self):
        return self.comma

class MyHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(MyHighlighter, self).__init__(parent)
        rules = []

        dictb = Diction().RetDictBuild()

        rules += [(r'%s' % w, 0, STYLES['buildin'])
        for w in dictb]
        
        dictdc = Diction().RetDictDefClass()
        
        rules +=[(r'%s' %w,  0,  STYLES['defclass'])
        for w in dictdc]
        
        rules +=[(r'\b%s\b\s*(\w+)' %w, 1, STYLES['dcname'])
        for w in dictdc]
        dictn = Diction().RetDictNumbers()
        
        rules +=[(r'\b%s\b' %w,  0,  STYLES['numbers'])
        for w in dictn]
        
        dictm = Diction().RetDictMath()
        
        rules +=[(r'\b%s\b' %w,  0,  STYLES['math'])
        for w in dictm]
        
        dictbr = Diction().RetDictBraces()
        
        rules +=[(r'%s' %w, 0, STYLES['braces'])
        for w in dictbr]
        
        self.rules = [(QRegExp(pat), index, fmt)
            for (pat, index, fmt) in rules]
            
            
    def highlightBlock( self, text ):
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)
            while index >= 0:
            # We actually want the index of the nth match
                index = expression.pos(nth)
                length = len(expression.cap(nth))#.length()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)
        self.setCurrentBlockState( 0 )

