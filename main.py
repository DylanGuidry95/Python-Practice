import sys, pygame
from cell import CellVisual
pygame.init()

size = width, height = 1080, 720
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

newCell = CellVisual((25, 25), (width/2,height/2), (255, 0, 0))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()    
    screen.fill(black)
    newCell.draw(screen)
    pygame.display.flip()
