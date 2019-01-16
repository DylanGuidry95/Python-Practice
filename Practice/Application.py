'''Application class'''
import pygame
from Drawing import Rectangle
from Vector2 import Vector2

class Application(object):
    def __init__(self, width, height):
        '''Constructor'''
        self.width = width
        self.height = height
        self.backgroun_color = [0,0,0]
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        

    def set_background_color(self, color):
        '''Changes the background color of window'''
        self.backgroun_color = color
        self.screen.fill(self.backgroun_color)
        pygame.display.flip()

    def update(self):
        '''Invoked every frame of the application'''
        shape = Rectangle(self.screen, [255,255,255], Vector2(150,150), 25,25)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            shape.draw()                    
            pygame.display.flip()


