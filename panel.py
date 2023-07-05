from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QToolButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class PanelSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.left_button = QToolButton()
        self.left_button.setArrowType(Qt.LeftArrow)
        layout = QHBoxLayout(self)
        layout.addWidget(self.left_button)
        self.setLayout(layout)

class HayDispenserPanel(QWidget):
    def __init__(self):
        super().__init__()

        #self.setWindowTitle("HorseFeeder 3000 control panel")
        self.num_locks = 6
        self.off_color = 'background-color : red'
        self.on_color = 'background-color : green'

    def init_panel(self):
        self.lock_labels = [f"Lock {i+1}" for i in range(self.num_locks)]
        self.buttons = [QPushButton(label) for label in self.lock_labels]
        self.labels = [QLabel(label) for label in self.lock_labels]
        #self.container = QWidget()
        layout = QVBoxLayout()
        for b,l in zip(self.buttons,self.labels):
            b.setCheckable(True)
            b.clicked.connect(self.was_toggled)
            b.setStyleSheet(self.off_color)
            layout.addWidget(b)
            layout.addWidget(l)
        #self.container.setLayout(layout)
        self.setLayout(layout)
        #self.setCentralWidget(self.container)

    def was_toggled(self,checked):
        if checked:
            self.sender().setStyleSheet(self.on_color)
        else:
            self.sender().setStyleSheet(self.off_color)
        print("Checked?", checked)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        disp_panel = HayDispenserPanel()
        disp_panel.num_locks=6
        disp_panel.init_panel()
        selector = PanelSelector()
        layout = QVBoxLayout()
        layout.addWidget(selector)
        layout.addWidget(disp_panel)
        self.container=QWidget()
        self.container.setLayout(layout)
        self.setCentralWidget(self.container)

