from board import Board
from NodeVisual import VisualNode

class VisualBoard(object):
    def __init__(self, surface, board):
        self.board = board
        self.surface = surface
        self.visual_nodes = []
        for node in board.nodes:
            self.visual_nodes.append(VisualNode(node, self.surface))
    
    def draw(self):
        for visual in self.visual_nodes:
            visual.draw()
            visual.update()