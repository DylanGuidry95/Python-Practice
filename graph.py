from node import Node

class Graph(object):
    def __init__(self, width, height):
        self.columns = width
        self.rows = height
        self.nodes = []

    def generate_nodes(self):
        for x in range(0,self.columns):
            for y in range(0, self.rows):
                self.nodes.append(Node([x,y]))

    def display_grid(self):
        counter = 0
        for x in range(0,self.columns):
            for y in range(0, self.rows):
                print str(self.nodes[counter].position[0]) + "," + str(self.nodes[counter].position[1])
                counter += 1