'''Application class'''
import pygame
from Drawing import Rectangle
from Vector2 import Vector2
from Vector2 import Rect

class Application(object):
    def __init__(self, width, height):
        '''Constructor'''
        self.width = width
        self.height = height
        self.backgroun_color = [0,0,0]
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.prev_time = 0.0
        self.time_between = 0.0
        self.running = True
        pygame.init()
        pygame.display.init()
        

    def set_background_color(self, color):
        '''Changes the background color of window'''
        self.backgroun_color = color
        self.screen.fill(self.backgroun_color)
        pygame.display.flip()

    def update(self):
        '''Invoked every frame of the application'''
        shape = Rectangle(self.screen, [255,255,255], Vector2(150,150), 25,25)
        while self.running:
            current_time = pygame.time.get_ticks()
            self.time_between = self.prev_time - current_time
            print(self.time_between)
            self.total_time = current_time
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if pygame.key.get_pressed()[pygame.K_w]:
                    shape.position = shape.position + (Vector2(0,10) * self.time_between)
            mouse_pos = Vector2(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[0])
            mouse_rect = Rect(mouse_pos, Vector2(1,1))
            if shape.rect.is_point_collision(mouse_pos):
                shape.change_color([0,255,0])
            else:
                shape.change_color([255,255,255])
            shape.draw()               
            pygame.display.flip()            


