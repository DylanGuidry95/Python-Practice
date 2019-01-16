import pygame
from Vector2 import Vector2
from Vector2 import Rect

class Shape(object):
    def __init__(self, surface, color, position):
        self.surface = surface
        self.color = color
        self.position = position

class Rectangle(Shape):
    def __init__(self, surface, color, postion, width, length) : 
        Shape.__init__(self, surface, color, postion)
        self.width = width
        self.lenght = length
        self.rect = Rect(Vector2(postion.x_pos - (width / 2), postion.y_pos - (length / 2)), Vector2(width, length))
    
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
