#pylint: disable=E1101

import pygame
from vector2 import vector2
import math

class Shape(object):
    def __init__(self, pos, col, surface):
        self.position = pos
        self.color = col
        self.draw_surface = surface

    def ChangeColor(self, col):
        self.color = col

class Rectangle(Shape):
    def __init__(self, pos, col, scale, surface):
        Shape.__init__(self, pos, col, surface)
        self.scale = scale

    def draw(self):
        pygame.draw.rect(self.draw_surface, (self.color[0], self.color[1], self.color[2]),
                         (self.position.x_pos, self.position.y_pos, self.scale[0], self.scale[1]))

class Circle(Shape):
    def __init__(self, pos, col, rad, surface):
        Shape.__init__(self, pos, col, surface)
        self.radius = rad

    def draw(self):
        pygame.draw.circle(self.draw_surface, (self.color[0], self.color[1], self.color[2]),
                           (self.position.x_pos, self.position.y_pos), self.radius)

class Line(Shape):
    def __init__(self, pos, col, length, surface):
        Shape.__init__(self, pos, col, surface)
        self.length = length

    def draw(self):
        pygame.draw.line(self.draw_surface, (self.color[0], self.color[1], self.color[2]),
                         (self.position.x_pos, self.position.y_pos), self.length)

class Ellipse(Shape):
    def __init__(self, pos, col, scale, surface):
        Shape.__init__(self, pos, col, surface)
        self.scale = scale

    def draw(self):
        pygame.draw.ellipse(self.draw_surface, (self.color[0], self.color[1], self.color[2]),
                            (self.position.x_pos, self.position.y_pos,
                             self.scale[0], self.scale[1]))

class Arc(Shape):
    def __init__(self, pos, col, scale, angles, thickness, surface):
        Shape.__init__(self, pos, col, surface)
        self.angles = [angles[0] * math.pi / 180, angles[1] * math.pi / 180]
        self.thickness = thickness
        self.scale = scale

    def draw(self):
        pygame.draw.arc(self.draw_surface, (self.color[0], self.color[1], self.color[2]),
                        (self.position.x_pos, self.position.y_pos,
                         self.scale[0], self.scale[1]),
                         self.angles[0], self.angles[1], self.thickness)

class Text(Shape):
    def __init__(self, pos, col, text, size, surface):
        Shape.__init__(self, pos, col, surface)
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont('arial', self.size)

    def draw(self):
        render = self.font.render(self.text, 0, (self.color[0], self.color[1], self.color[2]))
        self.draw_surface.blit(render, (self.position.x_pos, self.position.y_pos))