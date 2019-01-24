import pygame
from Vector2 import Vector2
from Vector2 import Rect

class Shape(object):
    def __init__(self, surface, color, position):
        self.surface = surface
        self.color = color
        self.position = position    

    def change_color(self, color):
        self.color = color

class Rectangle(Shape):
    def __init__(self, surface, color, position, width, length) : 
        Shape.__init__(self, surface, color, position)
        self.width = width
        self.length = length
        self.rect = Rect(Vector2(position.x_pos - (width / 2), position.y_pos - (length / 2)), Vector2(width, length))    

    def draw(self):
        self.rect = Rect(Vector2(self.position.x_pos - (self.width / 2), self.position.y_pos - (self.length / 2)), Vector2(self.width, self.length))
        pygame.draw.rect(self.surface, self.color, self.rect)
