from PyQt5.QtWidgets import *

class QScatterplotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setParent(parent)
        self.initUI()

    def initUI(self):
        self.noDataLabel = QLabel(self)
        self.noDataLabel.setText("No data received...")