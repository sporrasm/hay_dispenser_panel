from PyQt5.QtWidgets import QApplication
from panel import HayDispenserPanel
import sys

app=QApplication(sys.argv)
window=HayDispenserPanel()
window.init_panel()
window.show()
app.exec()
