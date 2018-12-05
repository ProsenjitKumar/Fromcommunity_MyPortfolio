import sys
from PyQt5.QtWidgets import (QWidget, QLineEdit, QGridLayout,QLabel, QApplication)
import pyqtgraph as pg
from ib_insync import *
util.useQt()

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=22)

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.edit = QLineEdit('TSLA', self)
        self.edit.editingFinished.connect(self.setTicker)
        self.label = QLabel('-', self)
        self.guiplot = pg.PlotWidget()
        self.guiplot.enableAutoRange()

        layout = QGridLayout(self)
        layout.addWidget(self.edit, 0, 0)
        layout.addWidget(self.label, 1, 0)
        layout.addWidget(self.guiplot, 2, 0, 3, 3)

        self.prevBar = None
        self.bars = None
        self.setTicker()
        ib.setCallback('updated', self.update)

    def setTicker(self):
        contract = Stock(self.edit.text(), 'SMART', 'USD')

        self.bars = ib.reqHistoricalData(
            contract,
            endDateTime='',
            durationStr='500 S',
            barSizeSetting='5 secs',
            whatToShow='MIDPOINT',
            useRTH=True,
            formatDate=1,
            keepUpToDate=True)
        self.update()

    def update(self):
        currBar = self.bars[-1] if self.bars else None
        if self.prevBar != currBar:
            self.prevBar = currBar
            self.label.setText(str(currBar))

            # Get only the close values
            bclose =  [b.close for b in self.bars]
            # Plot only last 100 items
            self.guiplot.plot(bclose[-100:], clear=True, )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())