# from https://doc.qt.io/qt-5/qtcharts-temperaturerecords-example.html
from PyQt5.QtC import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


a = QApplication([])

low = QBarSet("Min")
high = QBarSet("Max")

low << -52 << -50 << -45.3 << -37.0 << -25.6 << -8.0 << -6.0 << -11.8 << -19.7 << -32.8 << -43.0 << -48.0
high << 11.9 << 12.8 << 18.5 << 26.5 << 32.0 << 34.8 << 38.2 << 34.8 << 29.8 << 20.4 << 15.1 << 11.8

series = QStackedBarSeries()
series.append(low)
series.append(high)

chart = QChart()
chart.addSeries(series)
chart.setTitle("Temperature records in celcius")
chart.setAnimationOptions(QChart.SeriesAnimations)

categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

axis = QBarCategoryAxis()
axis.append(categories)
axis.setTitleText("Month")
chart.createDefaultAxes()
chart.setAxisX(axis, series)
chart.axisY(series).setRange(-52, 52)
chart.axisY(series).setTitleText("Temperature [&degC]")

chart.legend().setVisible(True)
chart.legend().setAlignment(Qt.AlignBottom)

chartView = QChartView(chart)
chartView.setRenderHint(QPainter.Antialiasing)

window = QMainWindow()
window.setCentralWidget(chartView)
window.resize(600, 300)
window.show()

a.exec_()