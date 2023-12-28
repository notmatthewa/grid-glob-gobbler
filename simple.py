import random
import time

COLORS = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']

def find_largest_blob(grid, row, col, color, visited, blob_cells):
 if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or visited[row][col]:
     return 0

 if grid[row][col] != color:
     return 0

 visited[row][col] = True

 blob_color = color
 blob_cells.append((row, col))

 blob_size = 1

 for dr, dc in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
     blob_size += find_largest_blob(grid, row + dr, col + dc, color, visited, blob_cells)

 return blob_size

def find_all_blobs(grid, color):
 visited = [[False]*len(grid[0]) for _ in range(len(grid))]
 max_blob_size = 0
 max_blob_color = None
 max_blob_cells = []

 for row in range(len(grid)):
     for col in range(len(grid[0])):
         blob_cells = []
         blob_size = find_largest_blob(grid, row, col, color, visited, blob_cells)
         if blob_size > max_blob_size:
             max_blob_size = blob_size
             max_blob_color = color
             max_blob_cells = blob_cells

 return max_blob_size, max_blob_color, max_blob_cells

def generate_grid(width, height):
    return [[random.choice(COLORS) for _ in range(width)] for _ in range(height)]

def print_grid(grid):
    for row in grid:
        print(row)

if __name__ == '__main__':
    grid = generate_grid(10000, 10000)

    start_time = time.time()

    max_blob_size, max_blob_color, max_blob_cells = find_all_blobs(grid, 'red')

    end_time = time.time()

    print('Time taken: ', end_time - start_time)
    print(max_blob_size, max_blob_color, max_blob_cells)