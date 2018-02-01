from A_Star.vector2 import Vector2
from shapes import *

class Graph_Visual(object):
    def __init__(self, graph, offset, scale):
        self.graph = graph
        self.node_visuals = []
        self.offset = offset
        self.scale = scale

    def set_up(self, screen):
        for node in self.graph.nodes:
            visual = Rectangle(node.position * self.offset, (255, 255, 255),
                               (self.scale[0], self.scale[1]), screen)
            self.node_visuals.append(visual)

    def draw(self):
        for visual in self.node_visuals:
            visual.draw()

    def update(self):
        for node in self.graph.nodes:
            if node.is_goal:
                self.node_visuals[self.graph.nodes.index(node)].change_color((255, 0, 0))
            if node.is_start:
                self.node_visuals[self.graph.nodes.index(node)].change_color((0, 255, 0))
            
