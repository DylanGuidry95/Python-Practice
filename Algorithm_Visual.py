'''File: Algorithm_Visual.py
   Name: Dylan Guidry
   Date: 2/1/2018'''
from shapes import Rectangle

class Graph_Visual(object):
    '''Visual representation for a graph of nodes'''
    def __init__(self, graph, offset, scale):
        self.graph = graph
        self.node_visuals = []
        self.offset = offset
        self.scale = scale

    def set_up(self, screen):
        '''Ensures all nodes are generated'''
        for node in self.graph.nodes:
            visual = Rectangle(node.position * self.offset, (255, 255, 255),
                               (self.scale[0], self.scale[1]), screen)
            self.node_visuals.append(visual)

    def draw(self):
        '''Draws the nodes to the screen'''
        for visual in self.node_visuals:
            visual.draw()

    def update(self):
        '''Updates the nodes color if they need to be'''
        for node in self.graph.nodes:
            if node.is_goal:
                self.node_visuals[self.graph.nodes.index(node)].change_color((255, 0, 0))
            if node.is_start:
                self.node_visuals[self.graph.nodes.index(node)].change_color((0, 255, 0))
