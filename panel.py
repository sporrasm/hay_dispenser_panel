from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QToolButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class PanelSelector(QWidget):
    def __init__(self,parent):
        super().__init__()
        self.left_button = QToolButton()
        self.right_button = QToolButton()
        self.left_button.setArrowType(Qt.LeftArrow)
        self.right_button.setArrowType(Qt.RightArrow)
        self.left_button.clicked.connect(self.move_left)
        self.right_button.clicked.connect(self.move_right)
        layout = QHBoxLayout(self)
        layout.addWidget(self.left_button)
        layout.addWidget(self.right_button)
        self.setLayout(layout)
        self.parent=parent 

    def move_left(self):
        self.parent.move_left()
        #if self.parent.panel_idx > 0:
        #    self.parent.panel_idx -= 1
        #else:
        #    self.parent.panel_idx=self.parent.num_panels-1
        #self.parent.update_panel()

    def move_right(self):
        self.parent.move_right()
        #if self.parent.panel_idx >= self.parent.num_panels-1:
        #    self.parent.panel_idx=0
        #else:
        #    self.parent.panel_idx += 1
        #self.parent.update_panel()

class HayDispenserPanel(QWidget):
    def __init__(self):
        super().__init__()

        #self.setWindowTitle("HorseFeeder 3000 control panel")
        self.num_locks = 6
        self.panel_idx=0
        self.off_color = 'background-color : red'
        self.on_color = 'background-color : green'

    def init_panel(self):
        self.lock_labels = [f"Lock {i+1}" for i in range(self.num_locks)]
        self.buttons = [QPushButton(label) for label in self.lock_labels]
        self.labels = [QLabel(label) for label in self.lock_labels]
        self.title=QLabel(f"Panel {self.panel_idx+1}")
        #self.container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.title)
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
        self.num_panels=3
        self.panel_idx=0
        selector = PanelSelector(self)
        layout = QVBoxLayout()
        layout.addWidget(selector)
        self.disp_panels = [HayDispenserPanel() for i in range(self.num_panels)]
        for i,panel in enumerate(self.disp_panels):
            panel.num_locks=6
            panel.panel_idx=i
            panel.init_panel()
            layout.addWidget(panel)
            if i == 0:
                panel.show()
            else:
                panel.hide()
        self.container=QWidget()
        self.container.setLayout(layout)
        self.setCentralWidget(self.container)

    def move_left(self):
        old=self.panel_idx
        if self.panel_idx > 0:
            self.panel_idx -= 1
        else:
            self.panel_idx=self.num_panels-1
        self.disp_panels[old].hide()
        self.disp_panels[self.panel_idx].show()
        #self.parent.update_panel()

    def move_right(self):
        old=self.panel_idx
        if self.panel_idx >= self.num_panels-1:
            self.panel_idx=0
        else:
            self.panel_idx += 1
        self.disp_panels[old].hide()
        self.disp_panels[self.panel_idx].show()

