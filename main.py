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
from algorithms.second_chance import secondChance

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys


class MainWindow(QWidget):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Page Replacement Algorithms Visualizor")

        # Create layouts
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        bottom_layout = QVBoxLayout()

        
        # Title Text
        title = QLabel("Page Replacement Algorithms Visualizor")
        title.setStyleSheet("QLabel { font-size: 22px; color: gray;}")
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
        self.dropdown_list.addItems(["FIFO", "LRU", "LFU", "OPTIMAL", "SECOND CHANCE"])
        top_layout.addWidget(self.dropdown_list)

        # Run Button
        run_button = QPushButton("Run")
        run_button.clicked.connect(self.run_algorithm)
        top_layout.addWidget(run_button)

        # Output Grid
        self.output_grid = QGridLayout()

        # Create the grid frame
        self.grid_frame = QFrame()
        self.grid_frame.setLayout(self.output_grid)
        self.grid_frame.setStyleSheet("border-width: 1;"
                               "border-radius: 0;"
                               "border-style: solid;"
                               "border-color: gray"
                               )
        bottom_layout.addWidget(self.grid_frame)

        # Page Faults Label
        self.page_fault_lbl = QLabel("")
        self.page_fault_lbl.setStyleSheet("QLabel { color : red; }")
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
                font-weight: bold;
            }

            QComboBox {
                background-color: #EEEEEE;
                border: none;
                padding: 5px;
            }

            QPushButton {
                background-color: #4CAF50;
                font-weight: bold;
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
                background-color: green;
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
        elif algorithm_name == "SECOND CHANCE":
            output_frames, output_page_fault = secondChance(sequence, frames)

        self.display_output(sequence, output_frames, output_page_fault)

    def display_output(self, sequence, output_frames, output_page_fault):
        """
        Function to display the output as a grid layout
        """
        # Clear previous output
        for i in reversed(range(self.output_grid.count())): 
            # Scan through the grid in reversed order so that you don't skip any items
            self.output_grid.itemAt(i).widget().deleteLater()

        # Display Page Access Sequence
        page_access_lbl = QLabel("Sequence:")
        page_access_lbl.setStyleSheet("QLabel { color : green; }")
        self.output_grid.addWidget(page_access_lbl, 0, 0)
        for i_page in range(len(sequence)):
            page_lbl = QLabel(str(sequence[i_page]))
            page_lbl.setStyleSheet("QLabel { color : green; }")
            self.output_grid.addWidget(page_lbl, 0, i_page + 1)

        # Display output frames
        for i_frame in range(1, len(output_frames)+1):
            frame_lbl = QLabel(f"Frame {i_frame}:")
            self.output_grid.addWidget(frame_lbl, i_frame, 0)

            for i_page in range(len(output_frames[i_frame-1])):
                page_lbl = QLabel(str(output_frames[i_frame-1][i_page]))
                
                # Set label color to red if its value is not equal to the previous value
                if (i_page > 0 and output_frames[i_frame-1][i_page] != output_frames[i_frame-1][i_page-1]) or (i_frame-1 == 0 and i_page == 0):
                    page_lbl.setStyleSheet("QLabel { color : red; }")
                
                if(output_frames[i_frame-1][i_page] != -1):
                    self.output_grid.addWidget(page_lbl, i_frame, i_page + 1)


        # Display total page faults
        self.page_fault_lbl.setText(f"Total Page Faults: {output_page_fault}")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    Root = MainWindow()
    Root.show()
    sys.exit(App.exec())




