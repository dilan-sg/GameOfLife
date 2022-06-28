import pygame
# RULES
# 1 or 0 neighbours = die (solitude/underpopulation)
# 2 or 3 neighbours = survive
# 4 or more (>3) = die (overpopulation)
# dead cell with ONLY 3 neighbours = live cell (reproduction)

# set up grid
# allow user to draw on grid
# run the program

width = height = 800
rows = columns = 400
cell_size = height // rows
black = (0,0,0)
white = (255,255,255)
def draw_grid(window):
    window.fill((0,0,0))
    for row in range(rows):
        for column in range(columns):
            pygame.draw.rect(window, (255,255,255), (row * cell_size, column * cell_size, cell_size, cell_size))
screen = pygame.display.set_mode((width, height))
draw_grid(screen)