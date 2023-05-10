##########################################
# Page Replacement Algorithms Visualization and Comparison
# Anas Ahmed Hassan Sayed
# Youssef Remah Mohamed
# Mohamed Abouelhadid
# Mariam sherif
##########################################

from algorithms.fifo import FIFO
from algorithms.lru import LRU
from algorithms.lfu import LFU
from algorithms.optimal import OPTIMAL

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys

##########################################
# GUI using PyQt6
##########################################
class MainWindow(QWidget):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()


##########################################
# Main
##########################################
if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())