# Cell Color Blob Finder

## Overview
The Cell Color Blob Finder is a Python visualization tool designed to find the largest contiguous area ("glob") of similarly colored cells in a grid. The project comprises several Python modules, each contributing to the overall functionality of the algorithm and its visualization.

## Modules

### `cell.py`
This module defines the `Cell` class, representing individual cells in the grid. Each cell has properties like coordinates, size, and color.

### `crawler.py`
The `Crawler` class in this module is responsible for navigating through the grid. It keeps track of visited cells and determines the size of contiguous color blobs.

### `grid.py`
The `Grid` class creates a grid of cells with specified dimensions. It initializes cells with random colors from a predefined set.

### `screen.py`
This module handles the Pygame-based visual representation of the grid and the blob-finding process. It initializes the game screen and manages the main loop for rendering.

### `main.py`
The entry point of the application. It launches the visualization screen and kicks off the blob-finding process.

## Setup and Execution

1. **Dependencies**: 
   - Python
   - Pygame

2. **Running the Application**:
   - Clone the repository.
   - Install Python and Pygame if not already installed.
   - Execute `python main.py` to start the application.

## Algorithm
The application visualizes an algorithm that scans a grid of randomly colored cells to find the largest contiguous blob of the same color. It uses the `Crawler` class to traverse the grid and keep track of the sizes of discovered blobs.

## Visualization
The visualization is powered by Pygame. It displays a grid of cells where each cell is colored randomly. As the algorithm runs, it highlights the currently explored blob and eventually indicates the largest blob found.
