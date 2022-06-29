import pygame
# RULES
# 1 or 0 neighbours = die (solitude/underpopulation)
# 2 or 3 neighbours = survive
# 4 or more (>3) = die (overpopulation)
# dead cell with ONLY 3 neighbours = live cell (reproduction)

# set up grid
# allow user to draw on grid
# run the program
'''
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
'''
black = (0, 0, 0)
white = (255, 255, 255)
width = height = 650

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
def main() :
    #main event loop that checks for pressed buttons
    screen.fill(white)
    #runs at good speed regardless of computer
    run = True
    while run:
        draw_Grid()
        clock.tick(60)
        for event in pygame.event.get() :
            #checks if any events have happened from the pygame module
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()

def draw_Grid() :
    s_size = 10
    for w in range(0, width, s_size) :
        for h in range(0, height, s_size) :
            rect = pygame.Rect(w, h, s_size, s_size)
            pygame.draw.rect(screen, black, rect, 1)
main()