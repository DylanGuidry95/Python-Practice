from Node import Node
from Drawing import Rectangle
from Vector2 import Vector2
import pygame

class VisualNode(object):
    def __init__(self, node, surface):
        self.node = node
        self.position = node.position * 10 + Vector2(5, 5)
        self.shape = Rectangle(surface, [255, 255, 255], self.position, 9, 9)

    def draw(self):
        self.shape.draw()

    def update(self):
        mouse_pos = Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]) 
        if self.shape.rect.is_point_collision(mouse_pos):
            self.shape.change_color([255,0,0])
        else:
            self.shape.change_color([255,255,255])