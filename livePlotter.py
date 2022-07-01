import logging, sys, webbrowser, traceback

from PyQt5 import QtWidgets, uic, QtCorefrom, QtTest
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDesktopWidget, QApplication, QSizePolicy
from PyQt5.QtCore import QObject, QTimer, QThread, pyqtSignal, pyqtSlot, QDate, QTime, QDateTime


logger = logging.getLogger()

ui_path = os.path.dirname(os.path.abspath(__file__))


class livePlotWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(midasWindow, self).__init__()
        uic.loadUi(os.path.join(ui_path, 'livePlot.ui'), self)


class getDataWorker(QThread):
    plotData = pyqtSignal()

    def __init__(self,pvList):
        super().__init__()
        self.pvList = pvList
        self.time = QTime.currentTime()
        self.data = np.zeros(len(pvList)+1)

    def run(self):

        while True:
            for pv in self.pvList:
                currVal = caget(pv)
                
            self.plotData.emit(np.array(QTime.currentTime(),self.data))
            QtTest.QTest.qWait(500)
            