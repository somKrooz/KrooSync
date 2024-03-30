import threading
import hou
from PySide2 import QtCore, QtWidgets, QtGui 
from .server import MyServer
import json
import os

class Sync(QtWidgets.QDialog):
    def __init__(self):
        super(Sync, self).__init__(hou.qt.mainWindow())
        self.server = None
        self.configure_dialog()
        self.widgets()
        self.layout()
        self.connection()

    def configure_dialog(self):
        width = 450
        height = 400

        self.setWindowTitle("KrooSync")
        self.setMinimumWidth(width) 
        self.setMinimumHeight(height)

        self.setMaximumWidth(width)
        self.setMaximumHeight(height)

    def widgets(self):
        self.checkbox = QtWidgets.QCheckBox('USD', self) 
        self.textEdit = QtWidgets.QLabel(self)


    def layout(self):
        self.mainlyt = QtWidgets.QVBoxLayout(self)   
        self.mainlyt.addWidget(self.checkbox)
        self.mainlyt.addWidget(self.textEdit)
        self.mainlyt.setAlignment(QtCore.Qt.AlignTop)
        self.mainlyt.setSpacing(10)
        self.mainlyt.setContentsMargins(20, 20, 20, 20)

    def connection(self):
        self.checkbox.clicked.connect(self.print)

    def print(self):
        state = {"USDstate": self.checkbox.isChecked()}
        home = hou.homeHoudiniDirectory()
        file_path = os.path.join(home, "scripts", "python", "KrooSync", "cache.json")
        with open(file_path, 'w') as f:
            json.dump(state, f)
                
    def Run(self):
        host = 'localhost'
        port = 13290
        self.server = MyServer(host, port)
        self.server.start()
        
    def showEvent(self, event):
        super(Sync, self).showEvent(event)
        t = threading.Thread(target=self.Run)
        t.start() 

    def closeEvent(self, event):
        state = {"USDstate": False}
        home = hou.homeHoudiniDirectory()
        file_path = os.path.join(home, "scripts", "python", "KrooSync", "cache.json")
        with open(file_path, 'w') as f:
            json.dump(state, f)

        if self.server:
            self.server.stop()
        event.accept()
