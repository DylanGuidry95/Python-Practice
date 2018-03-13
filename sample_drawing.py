import pygame
from shapes import Rectangle
from shapes import Line
from shapes import Text
from A_Star.node import Node
from A_Star.graph import Graph
from A_Star.vector2 import Vector2
from A_Star.a_star import AStar

class NodeVisual(object):
    def __init__(self, node, draw_pos, scale, draw_surface):
        self.node = node
        self.shape = Rectangle(draw_pos, (255, 255, 255), scale, draw_surface, 0)
        self.is_hoovered = False
        self.is_start = False
        self.is_goal = False
        self.is_path = False
        self.is_open = False
        self.is_closed = False
        self.show_scores = False
        self.border = Rectangle(draw_pos,(255, 255, 255), scale, draw_surface, 4)

    def update(self, events):
        self.node_clicked(events)                
        if not self.node.traversable:
            self.shape.change_color((0, 0, 0))
        elif self.is_closed and not self.is_start and not self.is_goal:
            self.shape.change_color((247, 143, 143))
        elif self.is_open and not self.is_start and not self.is_goal:
            self.shape.change_color((143, 183, 247))
        elif self.is_start:
            self.shape.change_color((0, 255, 0))
        elif self.is_goal:
            self.shape.change_color((255, 0, 0))
        else:
            self.shape.change_color((255, 255, 255))
        if self.is_hoovered:
            self.border.change_color((255, 0, 0))
        else:
            self.border.change_color((0, 0, 0))
            
    def reset_node(self):
        self.is_closed = False
        self.is_open = False
        self.is_path = False
        self.node.parent = None

    def draw(self, graph_visual):
        self.shape.draw()
        self.border.draw()        
        if self.node.parent is not None:
            par = graph_visual.get_visual(self.node.parent)
            line = pygame.draw.lines(self.shape.draw_surface, (0,255,0), True, 
            [[self.shape.position.x_pos + self.shape.scale[0] / 2, self.shape.position.y_pos + self.shape.scale[1] / 2],
            [par.shape.position.x_pos + par.shape.scale[0] / 2, par.shape.position.y_pos + par.shape.scale[1] / 2]], 1)
        if (self.is_open or self.is_closed or self.is_goal or self.is_start) and self.show_scores:
            text = Text(Vector2(5,5), (0,0,0), str(self.node.f_score), 12 , self.shape.draw_surface)
            text.draw_on_surface(self.shape.rect)
            text2 = Text(Vector2(25,20), (0,0,0), str(self.node.h_score), 12 , self.shape.draw_surface)
            text2.draw_on_surface(self.shape.rect)
            text3 = Text(Vector2(5,20), (0,0,0), str(self.node.g_score), 12 , self.shape.draw_surface)
            text3.draw_on_surface(self.shape.rect)

    def node_clicked(self, events):
        mouse_position = pygame.mouse.get_pos()
        if self.shape.rect.collidepoint(mouse_position):
            self.is_hoovered = True
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.node.traversable = not self.node.traversable            
        else:
            self.is_hoovered = False

class GraphVisual(object):
    def __init__(self, graph, node_offset, draw_Surface):
        self.graph = graph
        self.node_offset = node_offset
        self.draw_surface = draw_Surface
        self.node_visuals = []
        self.selected_node = None

    def gen_visual_nodes(self):
        count = 0
        for x in range(0, self.graph.columns * self.node_offset, self.node_offset):            
            for y in range(0, self.graph.rows * self.node_offset, self.node_offset):                  
                new_node = NodeVisual(self.graph[count], Vector2(x, y), 
                                      [35,35], self.draw_surface)
                if not new_node.node.traversable:
                    new_node.shape.change_color((100, 100, 100))
                self.node_visuals.append(new_node)               
                count += 1                       

    def update(self, events):
        for node in self.node_visuals:
            node.update(events)
            if node.is_hoovered:
                self.selected_node = node

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
        self.graph_visual = GraphVisual(self.algorithm.world, 40, surface)
        self.graph_visual.gen_visual_nodes()

    def update(self,events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.clear_nodes()
                    self.algorithm.update()
                if event.key == pygame.K_TAB:
                    for node in self.graph_visual.node_visuals:
                        node.show_scores = not node.show_scores
        for node in self.algorithm.open_list:
            visual = self.graph_visual.get_visual(node)
            if visual is not None:
                    visual.is_open = True
        for node in self.algorithm.closed_list:
            visual = self.graph_visual.get_visual(node)
            if visual is not None:
                visual.is_closed = True
        for node in self.algorithm.path:
            visual = self.graph_visual.get_visual(node)
            if visual is not None:
                visual.is_path = True        
        self.set_nodes(events)
        self.graph_visual.update(events)        

    def highlight_path(self):
        if self.algorithm.path is None:
            return
        path_visual_nodes = []
        for node in self.algorithm.path:
            visual = self.graph_visual.get_visual(node)
            if visual is not None:
                path_visual_nodes.append(visual)
        for visual in path_visual_nodes:
            parent_visual = self.graph_visual.get_visual(visual.node.parent)
            if parent_visual is not None:
                pygame.draw.lines(self.graph_visual.draw_surface, (255, 0, 255), True, 
                                         [[visual.shape.position.x_pos + (visual.shape.scale[0] / 2),
                                           visual.shape.position.y_pos + (visual.shape.scale[1] / 2)],
                                          [parent_visual.shape.position.x_pos + (parent_visual.shape.scale[0] / 2),
                                           parent_visual.shape.position.y_pos + (parent_visual.shape.scale[1] / 2)]], 4)
        return

    def clear_nodes(self):
        for node in self.graph_visual.node_visuals:            
            node.reset_node()

    def draw(self):
        self.graph_visual.draw()
        self.highlight_path()

    def set_nodes(self, events):    
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.graph_visual.selected_node.is_start = True
                    old = self.graph_visual.get_visual(self.algorithm.start_node)
                    if old is not None:
                        old.is_start = False
                    self.algorithm.start_node = self.graph_visual.selected_node.node                        
                if event.key == pygame.K_g:
                    self.graph_visual.selected_node.is_goal = True
                    old = self.graph_visual.get_visual(self.algorithm.goal_node)
                    if old is not None:
                        old.is_goal = False
                    self.algorithm.goal_node = self.graph_visual.selected_node.node

class Application(object):
    def __init__(self, step_delay, algorithm):
        pygame.init()
        self.step_delay = step_delay
        self.algorithm = algorithm
        self.screen = pygame.display.set_mode((1080, 720))    
        self.algorithm_visual = A_StarVisual(self.algorithm, self.screen)
        self.running = True
        self.events = None

    def update(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            pygame.event.pump()
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:    
                    self.running = False
            self.algorithm_visual.update(self.events)
            self.draw()

    def draw(self):
        self.algorithm_visual.draw()
        pygame.display.update()
        pygame.display.flip()   

def main():
    G = Graph(25,25)
    G.generate_nodes()
    algorithm = AStar(G)
    application = Application(0.5,algorithm)
    application.update()

main()