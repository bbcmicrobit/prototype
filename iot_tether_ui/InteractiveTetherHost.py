#!/usr/bin/python
#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import sys
import os
from PySide.QtGui import *
import PySide.QtGui as QtGui
import PySide.QtCore as QtCore
import traceback
import os
import subprocess
import signal
import random

editorLocation = (20,20,960,400)
consoleLocation = (20, 440, 960, 300)

class TextEdit(QMainWindow):

    def __init__(self):
        super(TextEdit, self).__init__()
        font = QFont("monospace", 9)
        font.setFixedPitch(True)
        self.setFont(font)
        self.filename = False
        self.Ui()

    def Ui(self):
        menus = {}
        actions = {}

        menubar = self.menuBar()
        menubar.setNativeMenuBar(True)
        self.toolbar = self.addToolBar("File")

        menus["menuFile"] = menuFile = menubar.addMenu('&File')
        menus["menuEdit"] = menuEdit = menubar.addMenu('&Edit')

        actions["newFile"] = QAction(QtGui.QIcon('add.png'), 'New', self)
        actions["newFile"].setShortcut('Ctrl+N')
        actions["newFile"].triggered.connect(self.newFile)
        self.toolbar.addAction(actions["newFile"])
        menuFile.addAction(actions["newFile"])
        menuFile.addSeparator()

        actions["openFile"] = QAction(QtGui.QIcon('fileopen.png'), 'Open', self)
        actions["openFile"].setShortcut('Ctrl+O')
        actions["openFile"].triggered.connect(self.openFile)
        self.toolbar.addAction(actions["openFile"])
        menuFile.addAction(actions["openFile"])

        actions["saveFile"] = QAction(QtGui.QIcon('filesave.png'), 'Save', self)
        actions["saveFile"].setShortcut('Ctrl+S')
        actions["saveFile"].triggered.connect(self.saveFile)
        self.toolbar.addAction(actions["saveFile"])
        menuFile.addAction(actions["saveFile"])
        menuFile.addSeparator()

        self.toolbar.addSeparator()

        actions["cutText"] = QAction(QtGui.QIcon('editcut.png'), 'Cut', self)
        actions["cutText"].setShortcut('Ctrl+X')
        actions["cutText"].triggered.connect(self.cutFunc)
        self.toolbar.addAction(actions["cutText"])
        menuEdit.addAction(actions["cutText"])

        actions["copyText"] = QAction(QtGui.QIcon('edit-copy.png'), 'Copy', self)
        actions["copyText"].setShortcut('Ctrl+C')
        actions["copyText"].triggered.connect(self.copyFunc)
        self.toolbar.addAction(actions["copyText"])
        menuEdit.addAction(actions["copyText"])

        actions["pasteText"] = QAction(QtGui.QIcon('editpaste.png'), 'Paste', self)
        actions["pasteText"].setShortcut('Ctrl+V')
        actions["pasteText"].triggered.connect(self.pasteFunc)
        self.toolbar.addAction(actions["pasteText"])
        menuEdit.addAction(actions["pasteText"])

        self.toolbar.addSeparator()
        menuEdit.addSeparator()

        actions["undoAction"] = QAction(QtGui.QIcon('undo.png'), 'Undo', self)
        actions["undoAction"].setShortcut('Ctrl+Z')
        actions["undoAction"].triggered.connect(self.undoFunc)
        self.toolbar.addAction(actions["undoAction"])
        menuEdit.addAction(actions["undoAction"])

        actions["redoAction"] = QAction(QtGui.QIcon('redo.png'), 'Redo', self)
        actions["redoAction"].setShortcut('Shift-Ctrl+Z')
        actions["redoAction"].triggered.connect(self.redoFunc)
        self.toolbar.addAction(actions["redoAction"])
        menuEdit.addAction(actions["redoAction"])

        self.toolbar.addSeparator()
        menuEdit.addSeparator()

        actions["runAction"] = QAction(QtGui.QIcon('run.png'), 'Run', self)
        actions["runAction"].setShortcut('Ctrl+R')
        actions["runAction"].triggered.connect(self.runFunc)
        self.toolbar.addAction(actions["runAction"])
        menuEdit.addAction(actions["runAction"])

        self.toolbar.addSeparator()

        self.action_TetherOn = QtGui.QAction(self)
        # self.actionHexfile.setIcon(QtGui.QIcon(":/icons/image1.xpm"))
        self.action_TetherOn.setObjectName("Tether on")
        # added this line:
        self.action_TetherOn.setIconText("Tether on")
        self.action_TetherOn.triggered.connect(self.program_tether)
        self.toolbar.addAction(self.action_TetherOn)

        self.action_TetherOff = QtGui.QAction(self)
        # self.actionHexfile.setIcon(QtGui.QIcon(":/icons/image1.xpm"))
        self.action_TetherOff.setObjectName("Tether off")
        # added this line:
        self.action_TetherOff.setIconText("Tether off")
        self.action_TetherOff.triggered.connect(self.programHexfile)
        self.toolbar.addAction(self.action_TetherOff)

        self.toolbar.addSeparator()

        actions["quitApp"] = QAction(QtGui.QIcon('window-close.png'), 'Quit', self)
        actions["quitApp"].setShortcut('Ctrl+Q')
        actions["quitApp"].triggered.connect(self.close)
        self.toolbar.addAction(actions["quitApp"])

        menuFile.addAction(actions["quitApp"])

        self.text = QTextEdit(self)
        self.setCentralWidget(self.text)
        self.setMenuWidget(menubar)
        self.setMenuBar(menubar)

        self.setGeometry(*editorLocation)
        self.setWindowTitle('Python Program Editor : [new]')
        self.show()

    def undoFunc(self):
        self.text.undo()

    def runFunc(self):
        print "TBD"
        filename = "".join([random.choice("qwertyuiopasdfghjklzxcvbnm") for _ in range(10)])

        f = open("/tmp/" + filename + ".py", 'w')
        filedata = self.text.toPlainText()
        f.write(filedata)
        f.close()

        console.runFile(filename)
        #self.text.undo()

    def programHexfile(self):
        # TBD
        print "TBD: Restore the hexfile that was running on the bug"
        print "TBD: or install a hexfile on the bug"

    def program_tether(self):
        # TBD
        print "TBD: Load the tether hexfile program_tether"

    def redoFunc(self):
        self.text.redo()

    def cutFunc(self):
        self.text.cut()

    def copyFunc(self):
        self.text.copy()

    def pasteFunc(self):
        self.text.paste()

    def unSaved(self):
        destroy = self.text.document().isModified()

        if destroy == False:
            return False
        else:
            detour = QMessageBox.question(self,
                                          "Hold your horses.",
                                          "File has unsaved changes. Save now?",
                                           QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            if detour == QMessageBox.Cancel:
                return True
            elif detour == QMessageBox.No:
                return False
            elif detour == QMessageBox.Yes:
                return self.saveFile()

        return True

    def saveFile(self):
        if self.filename is False:
            filename_tuple = QFileDialog.getSaveFileName(self, 'Save File', os.path.expanduser('~'))
            if filename_tuple[0] != "":
                print filename_tuple 
                self.filename = filename_tuple[0]

        if self.filename:
            f = open(self.filename, 'w')
            filedata = self.text.toPlainText()
            f.write(filedata)
            f.close()
            self.setWindowTitle('Python Program Editor : ' + self.filename)

    def newFile(self):
        if not self.unSaved():
            self.text.clear()
            self.filename = False
            self.setWindowTitle('Python Program Editor : [new]')

    def openFile(self):
        filename_tuple = QFileDialog.getOpenFileName(self, 'Open File', os.path.expanduser("~"))
        if filename_tuple[0] != "":
            self.filename = filename = filename_tuple[0]
            f = open(filename, 'r')
            filedata = f.read()
            self.text.setText(filedata)
            f.close()
            self.setWindowTitle('Python Program Editor : ' + self.filename)

    def closeEvent(self, event):
        if self.unSaved():
            event.ignore()
        else:
            console.close()
            #exit


class Console(QtGui.QPlainTextEdit):
    def __init__(self, prompt='$> ', startup_message='', parent=None):
        QtGui.QPlainTextEdit.__init__(self, parent)
        self.prompt = prompt
        self.history = []
        self.namespace = {}
        self.construct = []

        self.setGeometry(*consoleLocation)
        self.setWordWrapMode(QtGui.QTextOption.WrapAnywhere)
        self.setUndoRedoEnabled(False)
        self.document().setDefaultFont(QtGui.QFont("monospace", 9, QtGui.QFont.Normal))
        self.showMessage(startup_message)

        self.setWindowTitle('Python Interactive Console')

    def updateNamespace(self, namespace):
        self.namespace.update(namespace)

    def showMessage(self, message):
        self.appendPlainText(message)
        self.newPrompt()

    def newPrompt(self):
        if self.construct:
            prompt = '.' * len(self.prompt)
        else:
            prompt = self.prompt
        self.appendPlainText(prompt)
        self.moveCursor(QtGui.QTextCursor.End)

    def getCommand(self):
        doc = self.document()
        curr_line = unicode(doc.findBlockByLineNumber(doc.lineCount() - 1).text())
        curr_line = curr_line.rstrip()
        curr_line = curr_line[len(self.prompt):]
        return curr_line

    def runFile(self, filename):
        #console.runFile("/tmp/mpython.py")
        print "TBD 2", filename
        #filename = filename[5:-3]
        #filename = filename[5:-3]
        if True:
            tmp_stdout = sys.stdout

            class stdoutProxy():
                def __init__(self, write_func):
                    self.write_func = write_func
                    self.skip = False

                def write(self, text):
                    if not self.skip:
                        stripped_text = text.rstrip('\n')
                        self.write_func(stripped_text)
                        QtCore.QCoreApplication.processEvents()
                    self.skip = not self.skip

            sys.stdout = stdoutProxy(self.appendPlainText)
            sys.path = ["/tmp/"] + sys.path
            try:
                try:
                    x = __import__(filename)
                    #os.system("python " +filename)
                    #pro = subprocess.Popen("python " +filename,
                                           #stdout=sys.stdout,
                                           #shell=True,
                                           #preexec_fn=os.setsid)

                    #execfile(filename)
                    #result = eval(command, self.namespace, self.namespace)
                    #if result != None:
                    #    self.appendPlainText(repr(result))
                except SyntaxError:
                    exec command in self.namespace
            except SystemExit:
                self.close()
            except:
                traceback_lines = traceback.format_exc().split('\n')
                # Remove traceback mentioning this file, and a linebreak
                for i in (3,2,1,-1):
                    traceback_lines.pop(i)
                self.appendPlainText('\n'.join(traceback_lines))
            sys.stdout = tmp_stdout
            sys.path = sys.path[1:]

        self.newPrompt()
        self.moveCursor(QtGui.QTextCursor.End)
        try:
            os.unlink("/tmp/"+ filename + ".py")
        except:
            pass
        try:
            os.unlink("/tmp/"+ filename + ".pyc")
        except:
            pass



    def setCommand(self, command):
        if self.getCommand() == command:
            return
        self.moveCursor(QtGui.QTextCursor.End)
        self.moveCursor(QtGui.QTextCursor.StartOfLine, QtGui.QTextCursor.KeepAnchor)
        for i in range(len(self.prompt)):
            self.moveCursor(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor)
        self.textCursor().removeSelectedText()
        self.textCursor().insertText(command)
        self.moveCursor(QtGui.QTextCursor.End)

    def getConstruct(self, command):
        if self.construct:
            prev_command = self.construct[-1]
            self.construct.append(command)
            if not prev_command and not command:
                ret_val = '\n'.join(self.construct)
                self.construct = []
                return ret_val
            else:
                return ''
        else:
            if command and command[-1] == (':'):
                self.construct.append(command)
                return ''
            else:
                return command

    def getHistory(self):
        return self.history

    def setHisory(self, history):
        self.history = history

    def addToHistory(self, command):
        if command and (not self.history or self.history[-1] != command):
            self.history.append(command)
        self.history_index = len(self.history)

    def getPrevHistoryEntry(self):
        if self.history:
            self.history_index = max(0, self.history_index - 1)
            return self.history[self.history_index]
        return ''

    def getNextHistoryEntry(self):
        if self.history:
            hist_len = len(self.history)
            self.history_index = min(hist_len, self.history_index + 1)
            if self.history_index < hist_len:
                return self.history[self.history_index]
        return ''

    def getCursorPosition(self):
        return self.textCursor().columnNumber() - len(self.prompt)

    def setCursorPosition(self, position):
        self.moveCursor(QtGui.QTextCursor.StartOfLine)
        for i in range(len(self.prompt) + position):
            self.moveCursor(QtGui.QTextCursor.Right)

    def runCommand(self):
        command = self.getCommand()
        self.addToHistory(command)

        command = self.getConstruct(command)

        if command:
            tmp_stdout = sys.stdout

            class stdoutProxy():
                def __init__(self, write_func):
                    self.write_func = write_func
                    self.skip = False

                def write(self, text):
                    if not self.skip:
                        stripped_text = text.rstrip('\n')
                        self.write_func(stripped_text)
                        QtCore.QCoreApplication.processEvents()
                    self.skip = not self.skip

            sys.stdout = stdoutProxy(self.appendPlainText)
            try:
                try:
                    result = eval(command, self.namespace, self.namespace)
                    if result != None:
                        self.appendPlainText(repr(result))
                except SyntaxError:
                    exec command in self.namespace
            except SystemExit:
                self.close()
            except:
                traceback_lines = traceback.format_exc().split('\n')
                # Remove traceback mentioning this file, and a linebreak
                for i in (3,2,1,-1):
                    traceback_lines.pop(i)
                self.appendPlainText('\n'.join(traceback_lines))
            sys.stdout = tmp_stdout
        self.newPrompt()

    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
            self.runCommand()
            return
        if event.key() == QtCore.Qt.Key_Home:
            self.setCursorPosition(0)
            return
        if event.key() == QtCore.Qt.Key_PageUp:
            return
        elif event.key() in (QtCore.Qt.Key_Left, QtCore.Qt.Key_Backspace):
            if self.getCursorPosition() == 0:
                return
        elif event.key() == QtCore.Qt.Key_Up:
            self.setCommand(self.getPrevHistoryEntry())
            return
        elif event.key() == QtCore.Qt.Key_Down:
            self.setCommand(self.getNextHistoryEntry())
            return
        elif event.key() == QtCore.Qt.Key_D and event.modifiers() == QtCore.Qt.ControlModifier:
            self.close()
        super(Console, self).keyPressEvent(event)

    def closeEvent(self, event):
        editor.close()
        #exit

welcome_message = '''
   ---------------------------------------------------------------
         Python Interactive Console
   ---------------------------------------------------------------
'''


def main():
    global editor
    global console

    app = QApplication(sys.argv)
    editor = TextEdit()
    console = Console(startup_message=welcome_message)
    console.updateNamespace({'myVar1' : app, 'myVar2' : 1234})
    console.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
