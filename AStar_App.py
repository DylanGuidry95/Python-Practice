import pygame
import time
from Game_Loop.game import Application
from A_Star.a_star import AStar
from A_Star.graph import Graph
from Algorithm_Visual import Graph_Visual

class AStar_App(Application):
    def __init__(self, name, dim, grid_dim):
        Application.__init__(self, name, dim)
        self.graph = Graph(grid_dim[0], grid_dim[1])
        self.graph.generate_nodes()
        self.algorithm = AStar(self.graph)
        self.algorithm.set_goal_node(self.graph.nodes[len(self.graph.nodes) - 1])
        self.algorithm.set_start_node(self.graph.nodes[0])
        self.visual = Graph_Visual(self.algorithm, self.graph, 25, (10, 10))
        self.visual.set_up(self.screen)

    def update(self):
        if self.algorithm.start_up():
            goal = self.algorithm.update()
            while goal is None:
                time.sleep(1)
                goal = self.algorithm.update()
                self.visual.draw()
                self.visual.update()
                pygame.display.flip()
            current = goal
            while current is not None:
                print str(current.position.x_pos) + "," + str(current.position.y_pos)
                current = current.parent
                self.algorithm.goal_node = None

        return Application.update(self)
