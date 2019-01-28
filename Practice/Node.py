from Vector2 import Vector2

class Node(object):
    def __init__(self, position):
        self.position = position
        self.h_score = 0
        self.g_score = 0
        self.f_score = 0
        self.neighbors = []
        

    def get_neighbors(self, nodes):
        neighbors_pos = [Vector2(0, 1),
                        Vector2(0, -1),
                        Vector2(1, 0),
                        Vector2(-1, 0),
                        Vector2(1,1),
                        Vector2(-1, 1),
                        Vector2(1, -1),
                        Vector2(-1, -1)]    
        for node in nodes:
            if node.position == self.position:
                continue
            for pos in neighbors_pos:
                if node.position == pos + self.position:
                    self.neighbors.append(node)    