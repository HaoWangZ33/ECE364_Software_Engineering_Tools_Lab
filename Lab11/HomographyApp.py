#! /usr/bin/env python3.4
#
#$Author: ee364a07 $
#$Date: 2016-12-04 23:15:18 -0500 (Sun, 04 Dec 2016) $
#$Revision: 96178 $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/F16/students/ee364a07/Lab11/HomographyApp.py $
#$Id: HomographyApp.py 96178 2016-12-05 04:15:18Z ee364a07 $

#/opt/python3/current/lib/python3.4/site-packages/PySide/scripts
#python3.4 <file_path>/uic.py <input ".ui" file> -o <output ".py" file>

import operator
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from HomographyGUI import *

class HomographyGUI(QMainWindow, Ui_Dialog):

    def __init__(self, parent=None):
        super(HomographyGUI, self).__init__(parent)
        self.setupUi(self)
        self.sourcefile = ""
        self.targetfile = ""
        self.state = False

        self.setWindowTitle('ECE364 Final Project')
        self.pushButton.setText("Load Source...")
        self.pushButton_2.setText("Load Target...")
        self.lineEdit.setText("")
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEnabled(False)
        self.pushButton_3.setText("Acquire Points")
        self.pushButton_3.setEnabled(False)
        self.label.setEnabled(False)
        self.pushButton_4.setText("Transform")
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setText("Reset")
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setText("Save...")
        self.pushButton_6.setDisabled(True)
        self.graphicsView.setDisabled(True)
        self.graphicsView_2.setEnabled(False)
        self.comboBox.setEnabled(False)

        self.pushButton_5.clicked.connect(self.clear)
        self.pushButton.clicked.connect(self.load_source)
        self.pushButton_2.clicked.connect(self.load_target)
        self.pushButton_3.clicked.connect(self.acquire)


    def acquire(self):
        pass



    def load_source(self):
        self.sourcefile= self.loadData()
        self.source = QGraphicsScene(self)
        self.source.addPixmap(QPixmap(self.sourcefile))
        self.graphicsView.setScene(self.source)
        self.graphicsView.fitInView(self.source.sceneRect())

        if self.sourcefile != "" and self.targetfile != "":
            self.unlock()


    def load_target(self):
        self.targetfile = self.loadData()
        self.target = QGraphicsScene(self)
        self.target.addPixmap(QPixmap(self.targetfile))
        self.graphicsView_2.setScene(self.target)
        self.graphicsView_2.fitInView(self.target.sceneRect())

        if self.sourcefile != "" and self.targetfile != "":
            self.unlock()


    def unlock(self):
        self.pushButton_3.setEnabled(True)
        self.lineEdit.setEnabled(True)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)


    def clear(self):
        self.setWindowTitle('ECE364 Final Project')
        self.pushButton.setText("Load Source...")
        self.pushButton_2.setText("Load Target...")
        self.lineEdit.setText("")
        self.lineEdit.setEnabled(False)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setEnabled(False)
        self.pushButton_3.setText("Acquire Points")
        self.pushButton_3.setEnabled(False)
        self.label.setEnabled(False)
        self.pushButton_4.setText("Transform")
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setText("Reset")
        self.pushButton_5.setEnabled(False)
        self.pushButton_6.setText("Save...")
        self.pushButton_6.setDisabled(True)
        self.graphicsView.setDisabled(True)
        self.graphicsView_2.setEnabled(False)
        self.comboBox.setEnabled(False)


    def loadData(self):
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open png file ...', filter="png files (*.png)")

        if not filePath:
            return
        return filePath


if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = HomographyGUI()
    currentForm.show()
    currentApp.exec_()