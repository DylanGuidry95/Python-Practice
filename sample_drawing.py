import pygame
from shapes import Rectangle
from A_Star.node import Node
from A_Star.graph import Graph
from A_Star.vector2 import Vector2

class NodeVisual(object):
    def __init__(self, node, draw_pos, scale, draw_surface):
        self.node = node
        self.shape = Rectangle(draw_pos, (1, 1, 1), scale, draw_surface)

    def draw(self):
        self.shape.draw()

class GrpahVisual(object):
    def __init__(self, graph, node_offset, draw_Surface):
        self.graph = graph
        self.node_offset = node_offset
        self.draw_surface = draw_Surface
        self.node_visuals = []

    def gen_visual_nodes(self):
        count = 0
        for x in range(0, self.graph.columns * self.node_offset, self.node_offset):            
            for y in range(0, self.graph.rows * self.node_offset, self.node_offset):                  
                new_node = NodeVisual(self.graph[count], Vector2(x, y), 
                                      [25,25], self.draw_surface)
                self.node_visuals.append(new_node)               
                count += 1                       

    def draw(self):
        for node in self.node_visuals:
            node.draw()

pygame.init()

SCREEN = pygame.display.set_mode((1080, 720))
SCREEN.fill((255, 255, 255))

G = Graph(25,25)
G.generate_nodes()
GV = GrpahVisual(G, 30, SCREEN)
GV.gen_visual_nodes()

RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    GV.draw()

    pygame.display.flip()