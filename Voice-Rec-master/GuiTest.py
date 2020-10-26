# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui-Test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
#from PyQt5.QtMultimedia import QSound
#from speaker_recognition import task_predict
import sys
import os
import pyaudio
import wave
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
fname = "test/testfile.wav"

class Ui_windowTest(object):
    def setupUi(self, windowTest):
        windowTest.setObjectName("windowTest")
        windowTest.resize(490, 381)
        self.centralwidget = QtWidgets.QWidget(windowTest)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, -30, 531, 401))
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.test_record = QtWidgets.QPushButton(self.centralwidget)
        self.test_record.setGeometry(QtCore.QRect(70, 140, 141, 51))
        self.test_record.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.test_record.setObjectName("test_record")
        self.test_record.clicked.connect(self.record_audio)
        self.test_data = QtWidgets.QPushButton(self.centralwidget)
        self.test_data.setGeometry(QtCore.QRect(310, 220, 141, 51))
        self.test_data.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 85, 255);")
        self.test_data.setObjectName("test_data")
        self.test_data.clicked.connect(self.test_audio)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 10, 291, 41))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 24pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.speaker = QtWidgets.QLabel(self.centralwidget)
        self.speaker.setGeometry(QtCore.QRect(200, 290, 241, 31))
        self.speaker.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.speaker.setObjectName("speaker")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 290, 121, 31))
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(260, 140, 141, 51))
        self.play.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 0, 0);")
        self.play.setObjectName("play")
        self.play.clicked.connect(self.play_audio)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 70, 361, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 100, 351, 21))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 240, 261, 21))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        windowTest.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(windowTest)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 21))
        self.menubar.setObjectName("menubar")
        windowTest.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(windowTest)
        self.statusbar.setObjectName("statusbar")
        windowTest.setStatusBar(self.statusbar)

        self.retranslateUi(windowTest)
        QtCore.QMetaObject.connectSlotsByName(windowTest)

    def fun(): 
        return task_predict() 
    
    def retranslateUi(self, windowTest):
        _translate = QtCore.QCoreApplication.translate
        windowTest.setWindowTitle(_translate("windowTest", "MainWindow"))
        self.test_record.setText(_translate("windowTest", "Record"))
        self.test_data.setText(_translate("windowTest", "Test"))
        self.label_5.setText(_translate("windowTest", "Audio-File Testing"))
        #self.speaker.setText(_translate("windowTest", "Output to be displayed here"))
        #self.label_3.setText(_translate("windowTest", "This Speaker is:"))
        self.play.setText(_translate("windowTest", "Play"))
        self.label_2.setText(_translate("windowTest", "First, click \"Record\" button to record the speaker,"))
        self.label_4.setText(_translate("windowTest", "then \"Play\" to review the last recorded audio file"))
        self.label_6.setText(_translate("windowTest", "Click on \"Test\" to verify the speaker:"))

    def record_audio(self):
        testfile = "test/testfile.wav"
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        RECORD_SECONDS = 10
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
            data = stream.read(CHUNK)
            frames.append(data)
        print("")    
        print("**************DONE**************")
    
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        waveFile = wave.open(testfile, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
    
    def play_audio(self):
        print("..............Playback of Test File begins............")
        #QSound.play(fname)
        
        wf = wave.open(fname, 'rb')
        p = pyaudio.PyAudio()
        
        # open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

        # read data
        data = wf.readframes(CHUNK)

        # play stream (3)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        # stop stream (4)
        stream.stop_stream()
        stream.close()
        
        p.terminate()
        print("..............Playback of Test File ends..............")
    def test_audio(self):
        os.system('python speaker-recognition.py -t predict -i "test/testfile.wav" -m model.out')
        #os.system('python speaker-recognition.py -t predict -i "test/*.wav" -m model.out')
        #self.speaker.setText(task_predict)
        #speaker = QLabel(sound_file)
        #speaker.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    windowTest = QtWidgets.QMainWindow()
    ui = Ui_windowTest()
    ui.setupUi(windowTest)
    windowTest.show()
    sys.exit(app.exec_())

