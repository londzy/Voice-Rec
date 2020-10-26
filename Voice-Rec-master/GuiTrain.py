# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiTrain.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
#from PyQt5.QtWidgets import QLineEdit
import pyaudio
import wave
import sys
import os



class Ui_windowTrain(object):
    def setupUi(self, windowTrain):
        windowTrain.setObjectName("windowTrain")
        windowTrain.resize(503, 402)
        self.centralwidget = QtWidgets.QWidget(windowTrain)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-14, -28, 531, 431))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.train_record = QtWidgets.QPushButton(self.centralwidget)
        self.train_record.setGeometry(QtCore.QRect(180, 130, 141, 51))
        self.train_record.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.train_record.setObjectName("train_record")
        self.train_record.clicked.connect(self.record_audio)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 121, 41))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.train_data = QtWidgets.QPushButton(self.centralwidget)
        self.train_data.setGeometry(QtCore.QRect(190, 290, 141, 51))
        self.train_data.setStyleSheet("background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.train_data.setObjectName("train_data")
        self.train_data.clicked.connect(self.training)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 220, 311, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 260, 271, 16))
        self.label_4.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 0, 291, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.train_filename = QtWidgets.QLineEdit(self.centralwidget)
        self.train_filename.setGeometry(QtCore.QRect(180, 90, 241, 31))
        self.train_filename.setObjectName("train_filename")
        windowTrain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(windowTrain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 503, 21))
        self.menubar.setObjectName("menubar")
        windowTrain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(windowTrain)
        self.statusbar.setObjectName("statusbar")
        windowTrain.setStatusBar(self.statusbar)

        self.retranslateUi(windowTrain)
        QtCore.QMetaObject.connectSlotsByName(windowTrain)

    def retranslateUi(self, windowTrain):
        _translate = QtCore.QCoreApplication.translate
        windowTrain.setWindowTitle(_translate("windowTrain", "MainWindow"))
        self.train_record.setText(_translate("windowTrain", "Record"))
        self.label_2.setText(_translate("windowTrain", "File Name:"))
        self.train_data.setText(_translate("windowTrain", "Train Data"))
        self.label_3.setText(_translate("windowTrain", "Click on the \"Train Data\" button only when"))
        self.label_4.setText(_translate("windowTrain", "all sample voices have been recorded"))
        self.label_5.setText(_translate("windowTrain", "Audio-File Training"))

    def record_audio(self):
        file = "train/" + self.train_filename.text()+".wav"
        #path = "tr/" + file
        #fout = open(path, "w")
        print(file)
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 20
        #WAVE_OUTPUT_FILENAME = "F:\\development_set\test.wav"
        INPUT_DEVICE_INDEX=0

        audio = pyaudio.PyAudio()

        stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,input_device_index=INPUT_DEVICE_INDEX)

        print("..............RECORDING..............")

        frames = []

        for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK,  exception_on_overflow = False)
            frames.append(data)
        print("")
        print("****************DONE****************")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        waveFile = wave.open(file, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()

    def training(self):
        os.system('python speaker-recognition.py -t enroll -i "train/" -m model.out')
        #python speaker-recognition.py -t enroll -i "train/" -m model.out

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windowTrain = QtWidgets.QMainWindow()
    ui = Ui_windowTrain()
    ui.setupUi(windowTrain)
    windowTrain.show()
    sys.exit(app.exec_())
