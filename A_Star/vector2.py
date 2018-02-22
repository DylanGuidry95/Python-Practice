'''File: vector2.py
   Author: Dylan Guidry
   Date: 1/26/2018'''
import math

class Vector2(object):
    '''Vector class for 2d math'''
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y

    def __add__(self, other):
        new_vec = Vector2(self.x_pos + other.x_pos,
                          self.y_pos + other.y_pos)
        return new_vec

    def __sub__(self, other):
        new_vec = Vector2(self.x_pos - other.x_pos,
                          self.y_pos - other.y_pos)
        return new_vec

    def __mul__(self, other):
        new_vec = Vector2(self.x_pos * other,
                          self.y_pos * other)
        return new_vec

    def __eq__(self, other):
        return self.x_pos == other.x_pos and self.y_pos == other.y_pos

    def magnitude(self):
        '''Returns the magnitude of the vector'''
        mag = math.sqrt((self.x_pos + self.x_pos) + (self.y_pos + self.y_pos))
        return mag

    def normalize(self):
        '''Returns the vector in unit length'''
        new_vec = Vector2(self.x_pos / self.magnitude,
                          self.y_pos / self.magnitude)
        return new_vec
