''' File: a_star.py
    Author: Dylan Guidry
    Date: 1/24/2018'''
from graph import Graph
from node import Node

class AStar(object):
    '''Creates and object that will perform the A Star pathfinding algorithm'''
    def __init__(self, graph):
        self.world = graph
        self.start_node = None
        self.goal_node = None
        self.open_list = []
        self.closed_list = []
        self.current_node = None
        self.path = []

    def set_start_node(self, start):
        '''Sets the value of the start node for the algorithm'''
        if start in self.world.nodes:
            self.start_node = start
            self.start_node.change_state("start")
            self.current_node = self.start_node

    def set_goal_node(self, goal):
        '''Sets the value of the goal node for the algorithm'''
        if goal in self.world.nodes:
            self.goal_node = goal
            self.goal_node.change_state("goal")

    def set_wall(self, node):
        '''Replaces and removes non-traversable nodes in the algorithm'''
        if node in self.world.nodes:
            node.traversable = not node.traversable

    def check_nodes(self):
        '''Checks made sure no nodes are flagged as a start or goal that shouldn't be'''
        for node in self.world.nodes:
            if node.is_goal and self.goal_node is not node:
                node.change_state("goal")
            if node.is_start and self.start_node is not node:
                node.change_state("start")

    def get_neighbors(self):
        '''Returns a list of nodes that are neighboring the current node'''
        neighbors = []
        valid_neighbor = [[0, 1], [1, 0], [0, -1], [-1, 0],
                          [1, 1], [-1, -1], [-1, 1], [1, -1]]
        for node in self.world:
            for pos in valid_neighbor:
                if (self.current_node.position.x_pos + pos[0] is node.position.x_pos and
                        self.current_node.position.y_pos + pos[1] is node.position.y_pos and
                        node.traversable and
                        node not in self.closed_list):
                    neighbors.append(node)
        return neighbors

    def start_up(self):
        '''Checks to make sure the start and goal nodes are set up so the algorithm can run'''
        if self.start_node is None or self.goal_node is None:
            return False
        self.current_node = self.start_node
        self.open_list.append(self.current_node)
        return True

    def update(self, start, goal, graph):        
        '''A single step of the algorithm. This fucntion should be called everytime we want
        the algorithm to step through. If the complete condition is met the goal node is returned'''
        self.world = graph
        self.start_node = start
        self.open_list.append(self.start_node)
        self.goal_node = goal
        while self.goal_node not in self.closed_list or len(self.open_list) == 0:
            self.sort_open_list()
            if len(self.open_list) == 0:
                break
            self.current_node = self.open_list[0]
            self.open_list.remove(self.current_node)
            self.closed_list.append(self.current_node)
            if self.goal_node in self.closed_list:
                break
            neighbors = self.get_neighbors()
            for node in neighbors:
                node.calculate_g_score(self.current_node)
                node.calculate_h_score(self.goal_node)
                node.calculate_f_score()
                if node not in self.open_list:
                    self.open_list.append(node)
                else:
                    node.set_parent(self.current_node)
        self.path = []
        if self.closed_list.__contains__(self.goal_node):
            path_node = self.goal_node
            while path_node is not None:
                self.path.append(path_node)
                path_node = path_node.parent
        return self.path

    def sort_open_list(self):
        '''Sorts the node in the open list by the F Score from least to greatest'''
        self.open_list.sort(key=lambda node: node.f_score)
