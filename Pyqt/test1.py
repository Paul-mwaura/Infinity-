import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication,QMessageBox,QFileDialog
from PyQt5.QtGui import QIcon
import webbrowser

class Text_editor(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.copiedtext=""
        self.initUI()
        
        
    def initUI(self):               
        
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.textEdit.setText(" ")

        #Exiting Application
        exitAction = QAction(QIcon('close.png'),'Exit', self)
        exitAction.setShortcut('esc')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(self.close)
        
        #Creating a new file
        newAction=QAction(QIcon('file.png'),'New',self)
        newAction.setShortcut('Ctrl+N')
        newAction.setStatusTip('New File')
        newAction.triggered.connect(self.__init__)
        
        #Opening an existing File
        openAction=QAction(QIcon('open.png'),'Open',self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open File')
        openAction.triggered.connect(self.openo)
        
        #Saving a file
        saveAction=QAction(QIcon('save.png'),'Save',self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save File')
        saveAction.triggered.connect(self.save)
        
        undoAction=QAction(QIcon('undo.png'),'Undo',self)
        undoAction.setShortcut('Ctrl+Z')
        undoAction.setStatusTip('Undo')
        undoAction.triggered.connect(self.textEdit.undo)
        
        redoAction=QAction(QIcon('redo.png'),'Redo',self)
        redoAction.setShortcut('Ctrl+Y')
        redoAction.setStatusTip('Undo')
        redoAction.triggered.connect(self.textEdit.redo)
        
        copyAction=QAction(QIcon('copy.png'),'Copy',self)
        copyAction.setShortcut('Ctrl+C')
        copyAction.setStatusTip('Copy')
        copyAction.triggered.connect(self.copy)
        
        pasteAction=QAction(QIcon('paste.png'),'Paste',self)
        pasteAction.setShortcut('Ctrl+V')
        pasteAction.setStatusTip('Paste')
        pasteAction.triggered.connect(self.paste)
        
        cutAction=QAction(QIcon('scissors.png'),'Cut',self)
        cutAction.setShortcut('Ctrl+X')
        cutAction.setStatusTip('Cut')
        cutAction.triggered.connect(self.cut)
        
        aboutAction=QAction('About',self)
        aboutAction.setStatusTip('About')
        aboutAction.triggered.connect(self.about)
        
        self.statusBar()

        #Menu 
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)
        fileMenu2=menubar.addMenu('&Edit')
        fileMenu2.addAction(undoAction)
        fileMenu2.addAction(redoAction)
        fileMenu2.addAction(cutAction)
        fileMenu2.addAction(copyAction)
        fileMenu2.addAction(pasteAction)
        fileMenu3=menubar.addMenu('&Help')
        fileMenu3.addAction(aboutAction)
        

        tb1 = self.addToolBar('File')
        tb1.addAction(newAction)
        tb1.addAction(openAction)
        tb1.addAction(saveAction)
        
        tb2 = self.addToolBar('Edit')
        tb2.addAction(cutAction)
        tb2.addAction(copyAction)
        tb2.addAction(pasteAction)
        tb2.addAction(undoAction)
        tb2.addAction(redoAction)
        
        
        tb3 = self.addToolBar('Exit')
        tb3.addAction(exitAction)
        
        self.setGeometry(10,50,600,600)
        self.setWindowTitle('Infinity Editor')    
        self.setWindowIcon(QIcon('infinity icon.png')) 
        self.setStyleSheet("background-color:#f5d99e;""font:15px;""font-style:Segoe Ui;")
        self.show()
    
    
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit without Saving?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            self.statusBar().showMessage('Quiting...')
            event.accept()
            
        else:
            event.ignore()
            self.save()
            event.accept()
            
    def openo(self):
        self.statusBar().showMessage('Open Text Files ')
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        self.statusBar().showMessage('Open File')
        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)

    def save(self):
        self.statusBar().showMessage('Add extension to file name')
        fname =QFileDialog.getSaveFileName(self, 'Save File')
        data=self.textEdit.toPlainText()
        
        file=open(fname[0],'w')
        file.write(data)
        file.close()
    
    def copy(self):
        cursor=self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedtext=textSelected
    
    def paste(self):
        self.textEdit.append(self.copiedtext)
    
    def cut(self):
        cursor=self.textEdit.textCursor()
        textSelected=cursor.selectedText()
        self.copiedtext=textSelected
        self.textEdit.cut()
    
    def about(self):
        url ="https://en.wikipedia.org/wiki/Text_editor"
        self.statusBar().showMessage('Please wait...')
        webbrowser.open(url)
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Text_editor()
    sys.exit(app.exec_())