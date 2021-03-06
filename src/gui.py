# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from Timing import Timing
from functions import sleep
import sys
import time
import webbrowser

class Timer(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    progress = QtCore.pyqtSignal(int)
    timing = Timing()
    stop = True

    def setTiming(self, timing: Timing):
        self.timing = timing
        self.stop = False
    
    def hault(self):
        self.stop = True

    def run(self):
        while self.timing.getTimeInSeconds() >= 0:
            if self.stop:
                break
            self.progress.emit(self.timing)
            time.sleep(1)
            self.timing.changeTotalTime(-1)
        self.finished.emit()
        if not self.stop:
            sleep()

class Ui_MainWindow(object):
    running = False
    timing: Timing = Timing()
    
    def openGithub(self):
        webbrowser.open('https://github.com/Mahmoud217TR', new=2)

    def toggleRun(self):
        self.running = not self.running
        _translate = QtCore.QCoreApplication.translate
        if self.running:
            self.submitButton.setText(_translate("MainWindow", "Stop"))
            self.submitButton.setStyleSheet("color:rgb(255, 255, 255);\n"
"background-color:rgb(218, 105, 49);")
        else:
            self.submitButton.setText(_translate("MainWindow", "Start"))
            self.submitButton.setStyleSheet("color: rgb(23, 44, 61);\n"
"background-color: rgb(230, 179, 61);")
    
    def getHoursValue(self):
        return int(self.hoursBox.value())
    
    def getMinutesValue(self):
        return int(self.minutesBox.value())
    
    def getSecondsValue(self):
        return int(self.secondsBox.value())
    
    def setHoursValue(self, value:int):
        self.hoursLcd.setProperty("value", value)
    
    def setMinutesValue(self, value:int):
        self.minutesLcd.setProperty("value", value)
    
    def setSecondsValue(self, value:int):
        self.secondsLcd.setProperty("value", value)

    def setBoxesEnabled(self, value: bool = True):
        self.hoursBox.setProperty("enabled", value)
        self.minutesBox.setProperty("enabled", value)
        self.secondsBox.setProperty("enabled", value)

    def updateValues(self, timing):
        self.setSecondsValue(self.timing.getSeconds())
        self.setMinutesValue(self.timing.getMinutes())
        self.setHoursValue(self.timing.getHours())

    def startTimer(self):
        self.timer.setTiming(self.timing)
        self.setBoxesEnabled(False)
        self.thread.start()
            
    def stopTimer(self):
        self.timer.hault()

    def buttonPressed(self):
        if self.running:
            self.stopTimer()
        else:
            self.timing = Timing(self.getSecondsValue(), self.getMinutesValue(), self.getHoursValue())
            self.startTimer()
        self.toggleRun()

    def setupUi(self, MainWindow):
        # Threading
        self.thread = QtCore.QThread()
        self.timer = Timer()

        self.timer.moveToThread(self.thread)

        self.thread.started.connect(self.timer.run)
        self.timer.finished.connect(self.thread.quit)
        # self.timer.finished.connect(self.timer.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)
        self.timer.progress.connect(self.updateValues)

        self.thread.finished.connect(
            lambda: self.setBoxesEnabled(True)
        )
        
        # setup UI
        self.components(MainWindow)
        self.logoLabel.setPixmap(QtGui.QPixmap("artwork/Logo.png"))


        # Actions
        self.submitButton.clicked.connect(self.buttonPressed)
        self.actionGitHub.triggered.connect(self.openGithub)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sleep Timer"))
        self.sleepTimerLabel.setText(_translate("MainWindow", "Sleep Timer"))
        self.lcdSeperator1.setText(_translate("MainWindow", ":"))
        self.lcdSeperator2.setText(_translate("MainWindow", ":"))
        self.hoursLabel.setText(_translate("MainWindow", "Hours"))
        self.minutesLabel.setText(_translate("MainWindow", "Minutes"))
        self.secondsLabel.setText(_translate("MainWindow", "Seconds"))
        self.seperator1.setText(_translate("MainWindow", ":"))
        self.seperator2.setText(_translate("MainWindow", ":"))
        self.submitButton.setText(_translate("MainWindow", "Start"))
        self.menuAbout.setTitle(_translate("MainWindow", "MahmoudTR"))
        self.actionGitHub.setText(_translate("MainWindow", "GitHub"))

    # Easier to Change UI
    def components(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 607)
        MainWindow.setMinimumSize(QtCore.QSize(387, 607))
        MainWindow.setMaximumSize(QtCore.QSize(387, 607))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("artwork/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.98, y1:0.994682, x2:0, y2:0, stop:0 rgba(38, 72, 99, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.sleepTimerLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(42)
        self.sleepTimerLabel.setFont(font)
        self.sleepTimerLabel.setStyleSheet("color: rgb(23, 44, 61);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.sleepTimerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sleepTimerLabel.setObjectName("sleepTimerLabel")
        self.verticalLayout.addWidget(self.sleepTimerLabel)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.logoLabel = QtWidgets.QLabel(self.centralwidget)
        self.logoLabel.setMaximumSize(QtCore.QSize(126, 126))
        self.logoLabel.setText("")
        self.logoLabel.setPixmap(QtGui.QPixmap("artwork/Logo.png"))
        self.logoLabel.setScaledContents(True)
        self.logoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.logoLabel.setIndent(-2)
        self.logoLabel.setObjectName("logoLabel")
        self.horizontalLayout_5.addWidget(self.logoLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.minutesLcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.minutesLcd.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.minutesLcd.setFont(font)
        self.minutesLcd.setStyleSheet("color: rgb(218, 105, 49);\n"
"background-color: rgb(255, 255, 255);")
        self.minutesLcd.setFrameShape(QtWidgets.QFrame.Box)
        self.minutesLcd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.minutesLcd.setLineWidth(2)
        self.minutesLcd.setSmallDecimalPoint(False)
        self.minutesLcd.setDigitCount(2)
        self.minutesLcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.minutesLcd.setProperty("value", 0.0)
        self.minutesLcd.setObjectName("minutesLcd")
        self.gridLayout.addWidget(self.minutesLcd, 0, 2, 1, 1)
        self.lcdSeperator1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lcdSeperator1.setFont(font)
        self.lcdSeperator1.setStyleSheet("color: rgb(218, 105, 49);")
        self.lcdSeperator1.setAlignment(QtCore.Qt.AlignCenter)
        self.lcdSeperator1.setObjectName("lcdSeperator1")
        self.gridLayout.addWidget(self.lcdSeperator1, 0, 1, 1, 1)
        self.hoursLcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.hoursLcd.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hoursLcd.setFont(font)
        self.hoursLcd.setStyleSheet("color: rgb(218, 105, 49);\n"
"background-color: rgb(255, 255, 255);")
        self.hoursLcd.setLineWidth(2)
        self.hoursLcd.setSmallDecimalPoint(False)
        self.hoursLcd.setDigitCount(2)
        self.hoursLcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.hoursLcd.setProperty("value", 0.0)
        self.hoursLcd.setObjectName("hoursLcd")
        self.gridLayout.addWidget(self.hoursLcd, 0, 0, 1, 1)
        self.secondsLcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.secondsLcd.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.secondsLcd.setFont(font)
        self.secondsLcd.setStyleSheet("color: rgb(218, 105, 49);\n"
"background-color: rgba(255, 255, 255);")
        self.secondsLcd.setLineWidth(2)
        self.secondsLcd.setSmallDecimalPoint(False)
        self.secondsLcd.setDigitCount(2)
        self.secondsLcd.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.secondsLcd.setProperty("value", 0.0)
        self.secondsLcd.setObjectName("secondsLcd")
        self.gridLayout.addWidget(self.secondsLcd, 0, 4, 1, 1)
        self.hoursLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.hoursLabel.setFont(font)
        self.hoursLabel.setStyleSheet("color: rgb(23, 44, 61);")
        self.hoursLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hoursLabel.setObjectName("hoursLabel")
        self.gridLayout.addWidget(self.hoursLabel, 1, 0, 1, 1)
        self.lcdSeperator2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lcdSeperator2.setFont(font)
        self.lcdSeperator2.setStyleSheet("color: rgb(218, 105, 49);")
        self.lcdSeperator2.setAlignment(QtCore.Qt.AlignCenter)
        self.lcdSeperator2.setObjectName("lcdSeperator2")
        self.gridLayout.addWidget(self.lcdSeperator2, 0, 3, 1, 1)
        self.secondsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.secondsLabel.setFont(font)
        self.secondsLabel.setStyleSheet("color: rgb(23, 44, 61);")
        self.secondsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.secondsLabel.setObjectName("secondsLabel")
        self.gridLayout.addWidget(self.secondsLabel, 1, 4, 1, 1)
        self.minutesLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.minutesLabel.setFont(font)
        self.minutesLabel.setStyleSheet("color: rgb(23, 44, 61);")
        self.minutesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.minutesLabel.setObjectName("minutesLabel")
        self.gridLayout.addWidget(self.minutesLabel, 1, 2, 1, 1)
        self.hoursBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hoursBox.setFont(font)
        self.hoursBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hoursBox.setStyleSheet("color: rgb(23, 44, 61);\n"
"background-color: rgb(255, 255, 255);")
        self.hoursBox.setAlignment(QtCore.Qt.AlignCenter)
        self.hoursBox.setMaximum(24)
        self.hoursBox.setObjectName("hoursBox")
        self.gridLayout.addWidget(self.hoursBox, 2, 0, 1, 1)
        self.minutesBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.minutesBox.setFont(font)
        self.minutesBox.setStyleSheet("color: rgb(23, 44, 61);\n"
"background-color: rgb(255, 255, 255);")
        self.minutesBox.setAlignment(QtCore.Qt.AlignCenter)
        self.minutesBox.setMaximum(59)
        self.minutesBox.setObjectName("minutesBox")
        self.gridLayout.addWidget(self.minutesBox, 2, 2, 1, 1)
        self.secondsBox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.secondsBox.setFont(font)
        self.secondsBox.setStyleSheet("color: rgb(23, 44, 61);\n"
"background-color: rgb(255, 255, 255);")
        self.secondsBox.setAlignment(QtCore.Qt.AlignCenter)
        self.secondsBox.setReadOnly(False)
        self.secondsBox.setMaximum(59)
        self.secondsBox.setObjectName("secondsBox")
        self.gridLayout.addWidget(self.secondsBox, 2, 4, 1, 1)
        self.seperator2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.seperator2.setFont(font)
        self.seperator2.setAlignment(QtCore.Qt.AlignCenter)
        self.seperator2.setObjectName("seperator2")
        self.gridLayout.addWidget(self.seperator2, 2, 3, 1, 1)
        self.seperator1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.seperator1.setFont(font)
        self.seperator1.setStyleSheet("color: rgb(23, 44, 61);")
        self.seperator1.setAlignment(QtCore.Qt.AlignCenter)
        self.seperator1.setObjectName("seperator1")
        self.gridLayout.addWidget(self.seperator1, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setMinimumSize(QtCore.QSize(100, 99))
        self.submitButton.setMaximumSize(QtCore.QSize(100, 99))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("color: rgb(23, 44, 61);\n"
"background-color: rgb(230, 179, 61);")
        self.submitButton.setDefault(False)
        self.submitButton.setObjectName("submitButton")
        self.horizontalLayout_4.addWidget(self.submitButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 26))
        self.menubar.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGitHub = QtWidgets.QAction(MainWindow)
        self.actionGitHub.setCheckable(False)
        self.actionGitHub.setObjectName("actionGitHub")
        self.menuAbout.addAction(self.actionGitHub)
        self.menubar.addAction(self.menuAbout.menuAction())


def startApp():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    startApp()