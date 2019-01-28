'''Application class'''
import pygame
from Drawing import Rectangle
from Vector2 import Vector2
from Vector2 import Rect
from board import Board
from VisualBoard import VisualBoard

class Application(object):
    def __init__(self, width, height):
        '''Constructor'''
        self.width = width
        self.height = height
        self.background_color = [0, 0, 0]
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.delta_time = 0.0
        self.prev_time = 0.0
        self.running = True
        self.board = Board(25, 25)
        self.board_visual = VisualBoard(self.screen, self.board)
        pygame.init()
        pygame.display.init()


    def set_background_color(self, color):
        '''Changes the background color of window'''
        self.backgroun_color = color
        self.screen.fill(self.background_color)

    def update(self):
        '''Invoked every frame of the application'''              
        while self.running:
            #Refresh BackGround
            self.set_background_color(self.background_color)

            #Delta Time Calc
            current_time = pygame.time.get_ticks()
            self.delta_time = (current_time - self.prev_time) / 60.0
            self.prev_time = current_time

            #Event Polling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False                

            self.board_visual.draw()

            #Update screen            
            pygame.display.flip()
