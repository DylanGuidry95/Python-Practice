#pylint: disable=E1101

import pygame
from shapes import Rectangle
from shapes import Circle
from shapes import Text
from vector2 import vector2

pygame.init()

SCREEN = pygame.display.set_mode((1080, 720))
SCREEN.fill((255, 255, 255))

RECT = Rectangle(vector2(100, 100), (0, 255, 0), (100, 100), SCREEN)
CIRC = Circle(vector2(400, 400), (255, 0, 0), 50, SCREEN)
TEXT = Text(vector2(10, 10), (255, 0, 0), "Hello World", 24, SCREEN)



RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    RECT.draw()
    CIRC.draw()
    TEXT.draw()
    pygame.display.flip()
