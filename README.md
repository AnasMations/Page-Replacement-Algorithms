# Page Replacement Algorithms Visualization and Comparison

This repository contains a desktop application that visualizes and compares the behavior of different page replacement algorithms. The implemented algorithms are:

- First-In, First-Out (FIFO)
- Least Recently Used (LRU)
- Optimal (OPT)
- Least Frequently Used (LFU)

The desktop application is built using Python and PyQt6.

## Installation

To run the desktop application, you will need to have Python 3.x and PyQt6 installed on your machine.

```bash
pip install PyQt6
```

Once you have Python and PyQt6 installed, clone this repository to your local machine.

## Usage

To start the desktop application, open a terminal in the project directory and run the following command:

```bash
python main.py
```

This will start the application and you should see the main window.

To use the page replacement simulator, follow these steps:

1. Enter the page reference sequence in the input field. The sequence should be a string of integers separated by spaces.
2. Enter the number of frames in the input field.
3. Select the algorithm you want to use from the dropdown list.
4. Click the "Run Simulation" button to start the simulation.

The simulation will display the page frames and the page replacement process for the selected algorithm. The hit rate and fault rate will also be displayed.
