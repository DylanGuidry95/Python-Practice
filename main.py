import pygame
from AStar_App import AStar_App
from Algorithm_Visual import Graph_Visual

APP = AStar_App("Test", (1080, 720), (5, 5))
visual = Graph_Visual(APP.graph, 20, (10,10))
visual.set_up(APP.screen)
APP.start()

while APP.update():
    visual.draw()
    visual.update()
    pygame.display.flip()
