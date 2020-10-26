# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 00:05:29 2019

@author: User
"""

import sys
from GuiTrain import Ui_windowTrain
from GuiTest import Ui_windowTest
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi



class Recognition(QDialog):
    def __init__(self):
        super(Recognition, self).__init__()
        loadUi('GuiVoice.ui', self)
        
        self.train_window.clicked.connect(self.open_train)
        self.test_window.clicked.connect(self.open_test)
        self.exitButton.clicked.connect(self.close_window)        
    
    def open_train(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_windowTrain()
        self.ui.setupUi(self.window) 
        self.window.show()
        
        
    def open_test(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_windowTest()
        self.ui.setupUi(self.window) 
        self.window.show()
        
    
    def close_window(self):
        sys.exit()
        
        
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Recognition()
    window.setWindowTitle('RAPHTA (PTY) LTD - SPEAKER RECOGNITION SYSTEM')
    window.show()
    app.exit(app.exec_())