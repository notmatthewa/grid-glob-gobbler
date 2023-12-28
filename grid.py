from cell import Cell
import random

CELL_SIZE = 20
COLORS = (
    (255, 255, 200),
    (100, 100, 100)
)

class Grid:
    def __init__(self, width, height):
        """
        Initializes a Grid object with the specified width and height.

        Parameters:
        - width (int): The number of cells in the horizontal direction.
        - height (int): The number of cells in the vertical direction.
        """
        self.width = width
        self.height = height
        self.cells = [[Cell(i, j, CELL_SIZE, CELL_SIZE, random.choice(COLORS)) for j in range(height)] for i in range(width)]

    def get_cell(self, x, y):
        """
        Returns the cell at the specified coordinates.

        Parameters:
        - x (int): The x-coordinate of the cell.
        - y (int): The y-coordinate of the cell.

        Returns:
        - cell (Cell): The cell at the specified coordinates.
        """
        return self.cells[x][y]

    def get_adjacent_cells(self, x, y):
        """
        Returns a list of adjacent cells to the specified cell.

        Parameters:
        - x (int): The x-coordinate of the cell.
        - y (int): The y-coordinate of the cell.

        Returns:
        - adjacent_cells (list): A list of adjacent cells to the specified cell.
        """
        adjacent_cells = []
        if x > 0:
            adjacent_cells.append(self.cells[x - 1][y])
        if x < self.width - 1:
            adjacent_cells.append(self.cells[x + 1][y])
        if y > 0:
            adjacent_cells.append(self.cells[x][y - 1])
        if y < self.height - 1:
            adjacent_cells.append(self.cells[x][y + 1])
        return adjacent_cells

    def draw(self, win):
        """
        Draws the grid by calling the draw method of each cell.

        Parameters:
        - win (Window): The window to draw the grid on.
        """
        for row in self.cells:
            for cell in row:
                cell.draw(win)