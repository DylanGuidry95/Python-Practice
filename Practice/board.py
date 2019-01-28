from Node import Node
from Vector2 import Vector2

class Board(object):
    def __init__(self, width, height):
        self.nodes = []
        self.width = width
        self.height = height
        for x_pos in range(0, width):
            for y_pos in range(0, height):
                self.nodes.append(Node(Vector2(x_pos, y_pos)))
        for node in self.nodes:
            node.get_neighbors(self.nodes)