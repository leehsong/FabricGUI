from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime
import cv2

import numpy as np
import sys
import VideoCapture
import multiprocessing
import subprocess
import parse
import os
import sqlite3

class ScannerControlAPP(QtWidgets.QMainWindow, VideoCapture.Ui_CaptureBoard):
    beingCapture = 0
    imagename= {}
    bLoaded = 0
    productName = "NanoX"
    def __init__(self, parent=None):
        super(ScannerControlAPP, self).__init__(parent)
        self.entry = QtGui.QStandardItemModel()
        self.setupUi(self)
        self.pushCapture.clicked.connect(self.btnCapture)
        self.pushAnalysis.clicked.connect(self.btnAnalysis)
        self.comboBox.currentIndexChanged.connect(self.comboChange)
        scene = QtWidgets.QGraphicsScene(self)
        self.graphicsView.setScene(scene)
        self.comboitems()
        self.bLoaded =1

    def writeLog1(self, text):
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        print("date and time:", date_time)
        self.textEdit.append("[{T}], {str}".format(T=date_time, str=text))

    def comboChange(self):
        index = self.comboBox.currentIndex()
        print(self.comboBox.itemText(index))
        if self.bLoaded:
            fname = "images/{}".format(self.imagename[self.comboBox.itemText(index)])
            fname = fname.replace("/","\\")
            print(fname)
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap(fname)
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            scene.addItem(item)
            if  len(self.comboBox.itemText(index)) > 8 :
                self.productName = self.comboBox.itemText(index)[0:8]
            self.graphicsView.setScene(scene)

    def btnAnalysis(self):
        self.writeLog1("Button Analysis Clicked!")
        process0 = subprocess.Popen("python main.py")

    def runcapture(self, productname):
        if self.checkBox_0.isChecked():
            self.writeLog1("Camera [0] Start")
            process0 = subprocess.Popen("python grab_2camera.py scan 0 {} 1".format(productname))
        if self.checkBox_1.isChecked():
            self.writeLog1("Camera [1] Start")
            process1 = subprocess.Popen("python grab_2camera.py scan 1 {} 1 1".format(productname))
        if self.checkBox_2.isChecked():
            self.writeLog1("Camera [2] Start")
            process2 = subprocess.Popen("python grab_2camera.py scan 2 {} 2 1".format(productname))

    def btnCapture(self):
        print(sys.argv)

        if self.beingCapture: ## Code Stop
            self.writeLog1("Capture Stop")
            print("Capture Stop")
            self.pushCapture.setText("Start Capture")
            self.beingCapture = 0
            os.makedirs('stopframe')
        else:
            self.writeLog1("Capture Start")
            if os.path.isdir('stopframe'):
                os.rmdir('stopframe')
            self.beingCapture= 1
            print("Capture Start")
            self.pushCapture.setText("Stop Capture")
            self.runcapture(self.productName)
        print("Capture Button Clicked")

    def comboitems(self):
        ## Product name
        self.comboBox.addItem("NanoX_10A")
        self.imagename["NanoX_10A"] = "/images/NanoX_10A.png"


        ## 2018 database
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        for row in c.execute('SELECT * FROM app_textiles'):
            self.comboBox.addItem(row[2])
            self.imagename[row[2]] = row[14]

        print(self.imagename)

        scene = QtWidgets.QGraphicsScene(self)
        pixmap = QPixmap("textile_selected.png")
        item = QtWidgets.QGraphicsPixmapItem(pixmap)
        scene.addItem(item)
        self.graphicsView.setScene(scene)



def main():

    app = QApplication(sys.argv)
    form = ScannerControlAPP()
    form.show()
    app.exec_()



if __name__ == '__main__':
    main()