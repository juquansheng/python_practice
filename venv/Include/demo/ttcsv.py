# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
import csv
import numpy
import pandas as pd


class Ui_MainWindow(QtWidgets.QWidget):
    directory1 = ""
    seleceFiles = ""
    targetFileName = ""
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("csv")
        MainWindow.resize(500, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 100, 100, 50))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 100, 100, 50))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 300, 100, 50))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 300, 100, 50))
        self.pushButton_4.setObjectName("pushButton_4")

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 23))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.retranslateUi(MainWindow)

        self.pushButton.clicked.connect(self.selectForder)
        self.pushButton_2.clicked.connect(self.selectFiles)
        self.pushButton_3.clicked.connect(self.selectTargetPath)
        self.pushButton_4.clicked.connect(self.export)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.pushButton.setText(_translate("MainWindow", "选择文件夹"))
        self.pushButton_2.setText(_translate("MainWindow", "选择多文件"))
        self.pushButton_3.setText(_translate("MainWindow", "选择导出文件夹"))
        self.pushButton_4.setText(_translate("MainWindow", "导出"))


    def selectForder(self):
        global directory1
        global seleceFiles
        seleceFiles = False
        directory1 = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      "C:/Users/Administrator/Desktop")  # 起始路径
        print(directory1)

    def selectFiles(self):
        global directory1
        global seleceFiles
        directory1 = False
        seleceFiles, ok1 = QFileDialog.getOpenFileNames(self,
                                                  "多文件选择",
                                                  "C:/Users/Administrator/Desktop/新建文件夹",
                                                  "All Files (*);;Text Files (*.txt)")
        print(seleceFiles, ok1)

    def selectTargetPath(self):
        global targetFileName
        targetFileName =  QFileDialog.getSaveFileName(self,"save file","C:/Users/Administrator/Desktop/新建文件夹" ,"csv files (*.csv)")
        #targetFileName即为文件即将保存的绝对路径。形参中的第二个为对话框标题，第三个为打开后的默认给路径，第四个为文件类型过滤器
        print(targetFileName)

    def export(self):
        global seleceFiles
        global directory1
        global targetFileName

        resultColumn1 = []
        resultColumn2 = []
        resultColumn3 = []
        resultColumn4 = []

        print(seleceFiles)
        print(targetFileName[0])
        print(directory1)


        with open(targetFileName[0], 'w') as f:
            writeCSV = csv.writer(f)

        if(directory1):
            for root, dirs, files in os.walk(directory1):
                for filename in files:
                    with open(os.path.join(root, filename), 'r',encoding='UTF-8',errors='ignore') as s:
                        reader = csv.reader((line.replace('\0','') for line in s))
                        #reader1 = csv.DictReader(s)
                        column1 = []
                        column2 = []
                        column3 = []
                        column4 = []
                        rows = [row for row in reader]
                        for row in rows:
                            if(len(column1) < 8192):
                                column1.append(float(row[1]))
                                column2.append(float(row[2]))
                                column3.append(float(row[3]))
                                column4.append(float(row[4]))

                        #print(column1, column2, column3, column4)
                        sum1 = 0.0
                        sum2 = 0.0
                        sum3 = 0.0
                        sum4 = 0.0
                        for i in column1:
                            sum1 += numpy.square(i)
                        for i in column2:
                            sum2 += numpy.square(i)
                        for i in column3:
                            sum3 += numpy.square(i)
                        for i in column4:
                            sum4 += numpy.square(i)
                        resultColumn1.append(numpy.sqrt(sum1 / len(column1)))
                        resultColumn2.append(numpy.sqrt(sum2 / len(column1)))
                        resultColumn3.append(numpy.sqrt(sum3 / len(column1)))
                        resultColumn4.append(numpy.sqrt(sum4 / len(column1)))
                        print(resultColumn1, resultColumn2, resultColumn3, resultColumn4)
        if(seleceFiles):
            for files in seleceFiles:
                with open(files, 'r',encoding='UTF-8',errors='ignore') as s:
                    #reader = csv.reader(s)
                    reader = csv.reader((line.replace('\0', '') for line in s))
                    # reader1 = csv.DictReader(s)
                    column1 = []
                    column2 = []
                    column3 = []
                    column4 = []
                    rows = [row for row in reader]
                    for row in rows:
                        if (len(column1) < 8192):
                            column1.append(float(row[1]))
                            column2.append(float(row[2]))
                            column3.append(float(row[3]))
                            column4.append(float(row[4]))

                    # print(column1, column2, column3, column4)
                    sum1 = 0.0
                    sum2 = 0.0
                    sum3 = 0.0
                    sum4 = 0.0
                    for i in column1:
                        sum1 += numpy.square(i)
                    for i in column2:
                        sum2 += numpy.square(i)
                    for i in column3:
                        sum3 += numpy.square(i)
                    for i in column4:
                        sum4 += numpy.square(i)

                    resultColumn1.append(numpy.sqrt(sum1 / len(column1)))
                    resultColumn2.append(numpy.sqrt(sum2 / len(column1)))
                    resultColumn3.append(numpy.sqrt(sum3 / len(column1)))
                    resultColumn4.append(numpy.sqrt(sum4 / len(column1)))
                    print(resultColumn1, resultColumn2, resultColumn3, resultColumn4)
        dataframe = pd.DataFrame({'v1': resultColumn1, 'v2': resultColumn2, 'v3': resultColumn3, 'v4': resultColumn4})
        dataframe.to_csv(targetFileName[0] , index=False, sep=',')

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())