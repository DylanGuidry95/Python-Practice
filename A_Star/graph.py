''' File: graph.py
    Author: Dylan Guidry
    Date: 1/24/2018'''
from node import Node

class Graph(object):
    '''Class that create and object that represenents a 2D
    grid of node objects.'''
    def __init__(self, width, height):
        self.columns = width
        self.rows = height
        self.nodes = []

    def generate_nodes(self):
        '''Generates nodes based on the number of rows and columns the grid
        should have.'''
        for x in range(0, self.columns):
            for y in range(0, self.rows):
                self.nodes.append(Node([x, y]))

    def display_grid(self):
        '''Prints the position information of each node in the graph'''
        for node in self.nodes:
            print str(node.position[0]) + "," + str(node.position[1])
