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


class MainWindow(QWidget):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        # Create layouts
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        bottom_layout = QVBoxLayout()

        
        # Title Text
        title = QLabel("Page Replacement Algorithms Visualizor")
        layout.addWidget(title)

        # Frames Input
        frames_lbl = QLabel("Frames:")
        top_layout.addWidget(frames_lbl)
        self.frames_input = QLineEdit()
        top_layout.addWidget(self.frames_input)

        # Page Access Sequence Input
        sequence_lbl = QLabel("Page Access Sequence:")
        top_layout.addWidget(sequence_lbl)
        self.sequence_input = QLineEdit()
        top_layout.addWidget(self.sequence_input)

        # Dropdown List
        self.dropdown_list = QComboBox()
        self.dropdown_list.addItems(["FIFO", "LRU", "LFU", "OPTIMAL"])
        top_layout.addWidget(self.dropdown_list)

        # Run Button
        run_button = QPushButton("Run")
        run_button.clicked.connect(self.run_algorithm)
        top_layout.addWidget(run_button)

        # Output Labels
        output_lbl = QLabel("Output:")
        bottom_layout.addWidget(output_lbl)

        # Output Grid
        self.output_grid = QGridLayout()
        bottom_layout.addLayout(self.output_grid)

        # Page Faults Label
        self.page_fault_lbl = QLabel("")
        bottom_layout.addWidget(self.page_fault_lbl)

        # Add layouts to main layout
        layout.addLayout(top_layout)
        layout.addLayout(bottom_layout)

        # Set the main layout
        self.setLayout(layout)

        # Style Sheet
        style_sheet = """
            QWidget {
                background-color: #FFFFFF;
                font-family: Arial;
                font-size: 14px;
            }

            QLabel {
                color: #333333;
                font-size: 16px;
            }

            QComboBox {
                background-color: #EEEEEE;
                border: none;
                padding: 5px;
            }

            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 10px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
            }

            QPushButton:hover {
                opacity: 0.8;
            }

            QGridLayout {
                margin-top: 20px;
            }
        """
        App.setStyleSheet(style_sheet)  # Set style sheet to the application

    def run_algorithm(self):
        """"
        Function to run the selected algorithm
        """
        algorithm_name = self.dropdown_list.currentText()
        frames_str = self.frames_input.text()
        sequence_str = self.sequence_input.text()

        if not frames_str or not sequence_str:
            self.output_text.setPlainText("Please enter valid inputs")
            return

        frames = int(frames_str)
        sequence = list(map(int, sequence_str.split()))

        output_frames = []
        output_page_fault = 0

        if algorithm_name == "FIFO":
            output_frames, output_page_fault = FIFO(sequence, frames)
        elif algorithm_name == "LRU":
            output_frames, output_page_fault = LRU(sequence, frames)
        elif algorithm_name == "LFU":
            output_frames, output_page_fault = LFU(sequence, frames)
        elif algorithm_name == "OPTIMAL":
            output_frames, output_page_fault = OPTIMAL(sequence, frames)

        self.display_output(output_frames, output_page_fault)

    def display_output(self, output_frames, output_page_fault):
        """
        Function to display the output as a grid layout
        """
        # Clear previous output
        for i in reversed(range(self.output_grid.count())): 
            # Scan through the grid in reversed order so that you don't skip any items
            self.output_grid.itemAt(i).widget().deleteLater()

        # Display output frames
        for i_frame in range(len(output_frames)):
            frame_lbl = QLabel(f"Frame {i_frame +1}")
            self.output_grid.addWidget(frame_lbl, i_frame, 0)

            for i_page in range(len(output_frames[i_frame])):
                page_lbl = QLabel(str(output_frames[i_frame][i_page]))
                self.output_grid.addWidget(page_lbl, i_frame, i_page + 1)

        # Display total page faults
        self.page_fault_lbl.setText(f"Total Page Faults: {output_page_fault}")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())




