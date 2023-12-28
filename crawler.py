import pygame
from cell import Cell
from grid import Grid, CELL_SIZE

class Crawler:
    """
    A class representing a crawler object that explores a grid.

    Attributes:
    - width (int): The width of the grid.
    - height (int): The height of the grid.
    - grid (Grid): The grid object representing the cells.

    Methods:
    - __init__(self, width, height, grid): Initializes the crawler object.
    - reset_state(self): Resets the state of the crawler.
    - start_new_search(self): Starts a new search for a blob.
    - step(self): Performs a single step in the crawling process.
    - update_biggest_blob(self): Updates the biggest blob found so far.
    - draw(self, win): Draws the grid and the blobs on the window.
    - draw_x(self, win, cell): Draws an 'X' on the given cell.
    - draw_circle(self, win, cell): Draws a circle on the given cell.
    """
    def __init__(self, width, height, grid):
        self.width = width
        self.height = height
        self.grid = grid

        self.reset_state()

    def reset_state(self):
        """
        Resets the state of the crawler.
        """
        self.seen_globs = set()
        self.current_origin_cell = None
        self.biggest_glob = []
        self.biggest_glob_size = 0

        self.cells_to_visit = []
        self.current_blob = []
        self.current_seen_cells = set()

    def start_new_search(self):
        """
        Starts a new search for a blob.

        Returns:
        - bool: True if a new search is started, False otherwise.
        """
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid.get_cell(x, y)
                if cell not in self.seen_globs:
                    self.current_origin_cell = cell
                    self.cells_to_visit = [cell]
                    self.current_blob = []
                    self.current_seen_cells = set()
                    return True
        return False

    def step(self):
        """
        Performs a single step in the crawling process.

        Returns:
        - bool: True if a step is performed, False if the crawling is finished.
        """
        if not self.cells_to_visit:
            if not self.start_new_search():
                return False

        while self.cells_to_visit:
            cell = self.cells_to_visit.pop()
            self.current_seen_cells.add(cell)
            self.seen_globs.add(cell)

            if cell.get_color() == self.current_origin_cell.get_color():
                self.current_blob.append(cell)
                for adjacent_cell in self.grid.get_adjacent_cells(cell.x, cell.y):
                    if adjacent_cell not in self.current_seen_cells and adjacent_cell.get_color() == self.current_origin_cell.get_color():
                        self.cells_to_visit.append(adjacent_cell)

        if len(self.current_blob) > self.biggest_glob_size:
            self.update_biggest_blob()

        return True

    def update_biggest_blob(self):
        """
        Updates the biggest blob found so far.
        """
        for cell in self.biggest_glob:
            cell.unhighlight()
        
        self.biggest_glob = set(self.current_blob)
        self.biggest_glob_size = len(self.current_blob)
        for cell in self.biggest_glob:
            cell.highlight()

    def draw(self, win):
        """
        Draws the grid and the blobs on the window.

        Parameters:
        - win: The window to draw on.
        """
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid.get_cell(x, y)
                cell.draw(win)

        for cell in self.seen_globs:
            if cell not in self.biggest_glob:
                self.draw_x(win, cell)

        if self.current_origin_cell:
            self.draw_circle(win, self.current_origin_cell)

    def draw_x(self, win, cell):
        """
        Draws an 'X' on the given cell.

        Parameters:
        - win: The window to draw on.
        - cell: The cell to draw the 'X' on.
        """
        x, y = cell.x * CELL_SIZE, cell.y * CELL_SIZE
        pygame.draw.line(win, (0, 0, 0), (x, y), (x + CELL_SIZE, y + CELL_SIZE), 2)
        pygame.draw.line(win, (0, 0, 0), (x, y + CELL_SIZE), (x + CELL_SIZE, y), 2)

    def draw_circle(self, win, cell):
        """
        Draws a circle on the given cell.

        Parameters:
        - win: The window to draw on.
        - cell: The cell to draw the circle on.
        """
        center_x, center_y = cell.x * CELL_SIZE + CELL_SIZE // 2, cell.y * CELL_SIZE + CELL_SIZE // 2
        radius = CELL_SIZE // 2 - 2
        pygame.draw.circle(win, (0, 255, 0), (center_x, center_y), radius)
