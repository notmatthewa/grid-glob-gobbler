import pygame

class Cell:
    def __init__(self, x, y, w, h, color):
        """
        Initialize a Cell object.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
            w (int): The width of the cell.
            h (int): The height of the cell.
            color (tuple): The color of the cell in RGB format.

        Attributes:
            w (int): The width of the cell.
            h (int): The height of the cell.
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
            color (tuple): The color of the cell in RGB format.
            original_color (tuple): The original color of the cell.

        """
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.color = color
        self.original_color = color

    def draw(self, win):
        """
        Draw the cell on the given window.

        Args:
            win: The window to draw the cell on.

        """
        pygame.draw.rect(win, self.color, (self.x * self.w, self.y * self.h, self.w, self.h))

    def get_pos(self):
        """
        Get the position of the cell.

        Returns:
            tuple: The x and y coordinates of the cell.

        """
        return (self.x, self.y)

    def get_color(self):
        """
        Get the color of the cell.

        Returns:
            tuple: The color of the cell in RGB format.

        """
        return self.color

    def set_color(self, color):
        """
        Set the color of the cell.

        Args:
            color (tuple): The new color of the cell in RGB format.

        """
        self.color = color

    def highlight(self):
        """
        Highlight the cell by increasing its color intensity.

        """
        ADD_COLOR = 100
        self.color = (
            min(self.color[0] + ADD_COLOR, 255),
            min(self.color[1] + ADD_COLOR, 255),
            min(self.color[2] + ADD_COLOR, 255),
        )

    def unhighlight(self):
        """
        Restore the original color of the cell.

        """
        self.color = self.original_color

    def __repr__(self):
        """
        Return a string representation of the cell.

        Returns:
            str: A string representation of the cell.

        """
        return f"Cell({self.x}, {self.y}, {self.color})"