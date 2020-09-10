import PyQt5.QtCore
import PyQt5.QtGui
import PyQt5.QtWidgets
import sys

app = PyQt5.QtWidgets.QApplication(sys.argv)

widgetHello = PyQt5.QtWidgets.QWidget()
widgetHello.resize(480, 450)
widgetHello.setWindowTitle("Scanner Application")

LabHello = PyQt5.QtWidgets.QLabel(widgetHello)
LabHello.setText("Scanner Application")

font = PyQt5.QtGui.QFont()
font.setPointSize(12)
font.setBold(True)
LabHello.setFont(font)
size = LabHello.sizeHint()
LabHello.setGeometry(70,60,size.width(),size.height())

widgetHello.show()
sys.exit(app.exec_())
