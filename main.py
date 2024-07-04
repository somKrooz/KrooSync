import threading
import hou
from PySide2 import QtCore, QtWidgets  
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
        self.handle_hidden()

    def configure_dialog(self):
        width = 250
        height = 200

        self.setWindowTitle("KrooSync")
        self.setMinimumWidth(width) 
        self.setMinimumHeight(height)

        self.setMaximumWidth(width)
        self.setMaximumHeight(height)

    def widgets(self):
        self.checkbox = QtWidgets.QCheckBox('USD', self)
        self.Connectbox = QtWidgets.QCheckBox('Connect', self)  
        # self.matOptions = QtWidgets.QComboBox(self)
        self.matOptions.addItems(["Megascans"])
        self.matOptions.setCurrentIndex(0)


    def layout(self):

        self.mslyt = QtWidgets.QVBoxLayout(self)   
        # self.mslyt.addWidget(self.matOptions)
        self.mslyt.addWidget(self.Connectbox)  
        self.mslyt.addWidget(self.checkbox)
    
    def handle_hidden(self):
        home = hou.homeHoudiniDirectory()
        file_path = os.path.join(home, "scripts", "python", "KrooSync", "cache.json")
        with open(file_path, "r") as f:
            data = json.load(f)


    def connection(self):
        self.checkbox.clicked.connect(self.print)
        self.Connectbox.clicked.connect(self.print)
        self.Connectbox.clicked.connect(self.Checking_Handleing)
        self.matOptions.currentTextChanged.connect(self.print)



    def print(self):
        state = {"USDstate": self.checkbox.isChecked(),
                 "Checked": self.Connectbox.isChecked()}

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
        print("started....")
        # home = hou.homeHoudiniDirectory()
        # file_path = os.path.join(home, "scripts", "python", "KrooSync", "cache.json")
        # with open(file_path, "r") as f:
        #     data = json.load(f)
        #     state = data["Checked"]

        # if state==True:
        #     t = threading.Thread(target=self.Run)
        #     t.start() 

    def Checking_Handleing(self):
        home = hou.homeHoudiniDirectory()
        file_path = os.path.join(home, "scripts", "python", "KrooSync", "cache.json")
        with open(file_path, "r") as f:
            data = json.load(f)
            state = data["Checked"]

        if state == True:
            t = threading.Thread(target=self.Run)
            t.start() 
        if state == False:
            if self.server:
                self.server.stop()





    def closeEvent(self, event):
        state = {"USDstate": self.checkbox.isChecked(),
                "Checked": self.Connectbox.isChecked()}
        
        home = hou.homeHoudiniDirectory()
        file_path = os.path.join(home, "scripts", "python", "KrooSync", "cache.json")
        with open(file_path, 'w') as f:
            json.dump(state, f)

        home = hou.homeHoudiniDirectory()
        file_path = os.path.join(home, "scripts", "python", "KrooSync", "cache.json")
        with open(file_path, "r") as f:
            data = json.load(f)
            state = data["Checked"]
        print("Ended..")
        # if state==False:
        #     if self.server:
        #         self.server.stop()
        event.accept()
