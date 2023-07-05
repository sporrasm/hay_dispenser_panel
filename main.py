from PyQt5.QtWidgets import QApplication
from panel import MainWindow 
import sys

app=QApplication(sys.argv)
window=MainWindow()
#window.init_panel()
window.show()
app.exec()
