import pygame

class Vector2(object):
    def __init__(self, xPos, yPos):
        self.x_pos = xPos
        self.y_pos = yPos

    def __add__(self, other):
        return Vector2(self.x_pos + other.x_pos, self.y_pos + other.y_pos)

    def __sub__(self, other):
        return Vector2(self.x_pos - other.x_pos, self.y_pos - other.y_pos)

class Rect(object):
    def __init__(self, position, offset):
        self.rect = pygame.Rect(position.x_pos, position.y_pos, offset.x_pos, offset.y_pos)

    def is_point_collision(self, position):
        return self.rect.collidepoint(position.x_pos, position.y_pos)
        
    def is_rect_collision(self, rect):
        return self.rect.comntains(rect)
