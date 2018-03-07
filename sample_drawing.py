import pygame
from shapes import Rectangle
from shapes import Line
from A_Star.node import Node
from A_Star.graph import Graph
from A_Star.vector2 import Vector2
from A_Star.a_star import AStar

class NodeVisual(object):
    def __init__(self, node, draw_pos, scale, draw_surface):
        self.node = node
        self.shape = Rectangle(draw_pos, (255, 255, 255), scale, draw_surface)

    def draw(self, graph_visual):
        self.shape.draw()
        if self.node.parent is not None:
            par = graph_visual.get_visual(self.node.parent)
            line = pygame.draw.lines(self.shape.draw_surface, (0,255,0), True, 
            [[self.shape.position.x_pos + self.shape.scale[0] / 2, self.shape.position.y_pos + self.shape.scale[1] / 2],
            [par.shape.position.x_pos + par.shape.scale[0] / 2, par.shape.position.y_pos + par.shape.scale[1] / 2]])

class GraphVisual(object):
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
                if not new_node.node.traversable:
                    new_node.shape.change_color((100, 100, 100))
                self.node_visuals.append(new_node)               
                count += 1                       

    def draw(self):
        for node in self.node_visuals:
            node.draw(self)

    def get_visual(self, node):
        for node_visual in self.node_visuals:
            if node_visual.node == node:
                return node_visual
        return None

class A_StarVisual(object):
    def __init__(self, AStar, surface):
        self.algorithm = AStar
        self.graph_visual = GraphVisual(self.algorithm.world, 30, surface)
        self.graph_visual.gen_visual_nodes()

    def draw_open(self):
        for node in self.algorithm.open_list:
            visual = self.graph_visual.get_visual(node)
            if visual is not None:
                visual.shape.change_color((255, 0, 0))

    def draw_closed(self):
        for node in self.algorithm.closed_list:
            visual = self.graph_visual.get_visual(node)
            if visual is not None:
                visual.shape.change_color((0, 255, 0))
    
    def draw_path(self):
        for node in self.algorithm.path:
            visual = self.graph_visual.get_visual(node)
            if visual is not None:
                visual.shape.change_color((255, 0, 255))

    def draw_start_goal(self):
        start_visual = self.graph_visual.get_visual(self.algorithm.start_node)
        goal_visual = self.graph_visual.get_visual(self.algorithm.goal_node)
        start_visual.shape.change_color((150,255,150))
        goal_visual.shape.change_color((150,150,255))

pygame.init()

SCREEN = pygame.display.set_mode((1080, 720))
SCREEN.fill((0, 0, 0))

G = Graph(10,10)
G.generate_nodes()
G[11].traversable = False
G[1].traversable = False
A = AStar(G)
path = A.update(G[0], G[99], G)
GV = GraphVisual(G, 30, SCREEN)
GV.gen_visual_nodes()
AV = A_StarVisual(A,SCREEN)
AV.draw_open()
AV.draw_closed()
AV.draw_path()
AV.draw_start_goal()
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    

    AV.graph_visual.draw()

    pygame.display.update()
    pygame.display.flip()