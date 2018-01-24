from graph import Graph
from node import Node

class A_Star(object):
    def __init__(self, graph):
        self.world = graph
        self.start_node = None
        self.goal_node = None
        self.open_list = []
        self.closed_list = []
        self.current_node = None

    def set_start_node(self, start):
        if start in self.world.nodes:
            self.start_node = start
            self.start_node.change_state("start")
            self.current_node = self.start_node

    def set_goal_node(self, goal):
        if goal in self.world.nodes:
            self.goal_node = goal
            self.goal_node.change_state("goal")

    def set_wall(self, node):
        if node in self.world.nodes:
            node.traversable = not node.traversable

    def check_nodes(self):
        for node in self.world.nodes:
            if node.is_goal and self.goal_node is not node:
                node.change_state("goal")
            if node.is_start and self.start_node is not node:
                node.change_state("start")

    def get_neighbors(self):
        neighbors = []
        valid_neighbor = [[0, 1], [1, 0], [0, -1], [-1, 0],
                          [1, 1], [-1, -1], [-1, 1], [1, -1]]
        for node in self.world.nodes:
            for pos in valid_neighbor:
                if (self.current_node.position[0] + pos[0] is node.position[0] and
                        self.current_node.position[1] + pos[1] is node.position[1]):
                    neighbors.append(node)
        return neighbors
