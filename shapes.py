'''File: shapes.py
   Author: Dylan Guidry
   Date: 1/26/2018'''
#pylint: disable=E1101

import math
import pygame
from A_Star.vector2 import Vector2

class Shape(object):
    '''Base class for drawing all shapes'''
    def __init__(self, pos, col, surface):
        self.position = pos
        self.color = col
        self.draw_surface = surface
        self.pygame_object = None

    def change_color(self, col):
        '''Allows the changing of the shapes color without accessing
        the variable'''
        self.color = col

class Rectangle(Shape):
    '''Class that will allow the user to draw a rectangle to the screen'''
    def __init__(self, pos, col, scale, surface, width):
        Shape.__init__(self, pos, col, surface)
        self.scale = scale
        self.width =width
        self.rect = pygame.rect.Rect((self.position.x_pos, self.position.y_pos,
                                      self.scale[0], self.scale[1]))

    def draw(self):
        '''Draws a rectangle to the screen based on the properties the user declared'''
        self.pygame_object = pygame.draw.rect(self.draw_surface, (self.color[0], self.color[1], self.color[2]),
                         (self.position.x_pos, self.position.y_pos, self.scale[0], self.scale[1]), self.width)

class Circle(Shape):
    '''Class that will allow the user to draw a circle to the screen'''
    def __init__(self, pos, col, rad, surface):
        Shape.__init__(self, pos, col, surface)
        self.radius = rad

    def draw(self):
        '''Draws a circle to the screen based on the properties the user declared'''
        pygame.draw.circle(self.draw_surface, (self.color[0], self.color[1], self.color[2]),
                           (self.position.x_pos, self.position.y_pos), self.radius)

class Line(Shape):
    '''Class that will allow the user to draw a line to the screen'''
    def __init__(self, pos, col, length, surface):
        Shape.__init__(self, pos, col, surface)
        self.length = length

    def draw(self):
        '''Draws a line to the screen based on the properties the user declared'''
        pygame.draw.line(self.draw_surface, (self.color[0], self.color[1], self.color[2]),
                         (self.position.x_pos, self.position.y_pos), self.length)

class Ellipse(Shape):
    '''Class that will allow the user to draw a ellipse to the screen'''
    def __init__(self, pos, col, scale, surface):
        Shape.__init__(self, pos, col, surface)
        self.scale = scale

    def draw(self):
        '''Draws a ellipse to the screen based on the properties the user declared'''
        pygame.draw.ellipse(self.draw_surface, (self.color[0], self.color[1], self.color[2]),
                            (self.position.x_pos, self.position.y_pos,
                             self.scale[0], self.scale[1]))

class Arc(Shape):
    '''Class that will allow the user to draw a arc to the screen'''
    def __init__(self, pos, col, scale, angles, thickness, surface):
        Shape.__init__(self, pos, col, surface)
        self.angles = [angles[0] * math.pi / 180, angles[1] * math.pi / 180]
        self.thickness = thickness
        self.scale = scale

    def draw(self):
        '''Draws a arc to the screen based on the properties the user declared'''
        pygame.draw.arc(self.draw_surface, (self.color[0], self.color[1], self.color[2]),
                        (self.position.x_pos, self.position.y_pos,
                         self.scale[0], self.scale[1]),
                        self.angles[0], self.angles[1], self.thickness)

class Text(Shape):
    '''Class that will allow the user to draw text to the screen'''
    def __init__(self, pos, col, text, size, surface):
        Shape.__init__(self, pos, col, surface)
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont('arial', self.size)

    def draw(self):
        '''Draws text to the screen based on the properties the user declared'''
        render = self.font.render(self.text, 0, (self.color[0], self.color[1], self.color[2]))
        self.draw_surface.blit(render, (self.position.x_pos, self.position.y_pos))

    def draw_on_surface(self, rect):
        '''Draws text to the screen based on the properties the user declared'''
        render = self.font.render(self.text, 0, (self.color[0], self.color[1], self.color[2]))
        self.draw_surface.blit(render, (rect[0] + self.position.x_pos, rect[1] + self.position.y_pos))
