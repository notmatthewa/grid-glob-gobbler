import pygame
from grid import Grid, CELL_SIZE
from crawler import Crawler

def main_screen():
    pygame.init()

    WIDTH, HEIGHT = 50, 50
    WINDOW_SIZE = (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE)

    win = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("Cell Color Blob Finder")

    grid = Grid(WIDTH, HEIGHT)
    crawler = Crawler(WIDTH, HEIGHT, grid)

    clock = pygame.time.Clock()
    FPS = 60

    run = True
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False

        if not crawler.step():
            run = False

        win.fill((0, 0, 0))
        crawler.draw(win)

        pygame.display.set_caption("Cell Color Blob Finder - Biggest Blob Size: " + str(len(crawler.biggest_glob)))

        pygame.display.update()

    min_x = min(cell.x for cell in crawler.biggest_glob)
    max_x = max(cell.x for cell in crawler.biggest_glob)
    min_y = min(cell.y for cell in crawler.biggest_glob)
    max_y = max(cell.y for cell in crawler.biggest_glob)

    cell_size = min(WINDOW_SIZE[0] / (max_x - min_x + 1), WINDOW_SIZE[1] / (max_y - min_y + 1))

    win = pygame.display.set_mode((int((max_x - min_x + 1) * cell_size), int((max_y - min_y + 1) * cell_size)))
    pygame.display.set_caption("Biggest Blob")

    for cell in crawler.biggest_glob:
        cell.x -= min_x
        cell.y -= min_y
        cell.w = cell_size
        cell.h = cell_size

    while True:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()

        win.fill((0, 0, 0), (0, 0, win.get_width(), win.get_height()))
        for cell in crawler.biggest_glob:
            cell.draw(win)

        pygame.display.update()