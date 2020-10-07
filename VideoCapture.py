# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoCapture.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CaptureBoard(object):
    def setupUi(self, CaptureBoard):
        CaptureBoard.setObjectName("CaptureBoard")
        CaptureBoard.resize(480, 766)
        self.buttonBox = QtWidgets.QDialogButtonBox(CaptureBoard)
        self.buttonBox.setGeometry(QtCore.QRect(0, 720, 461, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(CaptureBoard)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 181, 131))
        self.groupBox.setObjectName("groupBox")
        self.checkBox_0 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_0.setGeometry(QtCore.QRect(30, 30, 81, 16))
        self.checkBox_0.setObjectName("checkBox_0")
        self.checkBox_1 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_1.setGeometry(QtCore.QRect(30, 60, 81, 16))
        self.checkBox_1.setObjectName("checkBox_1")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.graphicsView = QtWidgets.QGraphicsView(CaptureBoard)
        self.graphicsView.setGeometry(QtCore.QRect(30, 210, 421, 311))
        self.graphicsView.setObjectName("graphicsView")
        self.pushCapture = QtWidgets.QPushButton(CaptureBoard)
        self.pushCapture.setGeometry(QtCore.QRect(250, 20, 201, 61))
        self.pushCapture.setObjectName("pushCapture")
        self.textEdit = QtWidgets.QTextEdit(CaptureBoard)
        self.textEdit.setGeometry(QtCore.QRect(30, 540, 421, 171))
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(CaptureBoard)
        self.comboBox.setGeometry(QtCore.QRect(30, 170, 421, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushAnalysis = QtWidgets.QPushButton(CaptureBoard)
        self.pushAnalysis.setGeometry(QtCore.QRect(250, 90, 201, 61))
        self.pushAnalysis.setObjectName("pushAnalysis")

        self.retranslateUi(CaptureBoard)
#        self.buttonBox.accepted.connect(CaptureBoard.accept)
#        self.buttonBox.rejected.connect(CaptureBoard.reject)
        QtCore.QMetaObject.connectSlotsByName(CaptureBoard)

    def retranslateUi(self, CaptureBoard):
        _translate = QtCore.QCoreApplication.translate
        CaptureBoard.setWindowTitle(_translate("CaptureBoard", "CaptureControl"))
        self.groupBox.setTitle(_translate("CaptureBoard", "Scanner Selection"))
        self.checkBox_0.setText(_translate("CaptureBoard", "Camera0"))
        self.checkBox_1.setText(_translate("CaptureBoard", "Camera1"))
        self.checkBox_2.setText(_translate("CaptureBoard", "Camera2"))
        self.pushCapture.setText(_translate("CaptureBoard", "Capture"))
        self.pushAnalysis.setText(_translate("CaptureBoard", "Analysis"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CaptureBoard = QtWidgets.QDialog()
    ui = Ui_CaptureBoard()
    ui.setupUi(CaptureBoard)
    CaptureBoard.show()
    sys.exit(app.exec_())

