from shapes import Rectangle
from shapes import Circle
from shapes import Line
from vector2 import Vector2
from node import Node

class VisualNode(object):
    def __init__(self, pos, scale, open_color, closed_color, current_color, color, node, screen):
        self.position = pos
        self.open_color = open_color
        self.closed_color = closed_color
        self.current_color = current_color
        self.color = color
        self.node = node
        self.rectangle = Rectangle(pos, color, scale, screen)

    def draw_node(self):
        self.rectangle.draw()
        if self.node.parent is not None:
            circle = Circle(self.position, (0, 0, 0), self.rectangle.scale[0],
                            self.rectangle.draw_surface)
            circle.draw()
            line = Line(self.position, (0, 0, 0), self.rectangle.scale[0] * 2,
                        self.rectangle.draw_surface)
            line.draw()


    def change_state(self, state):
        if state == "open_list":
            self.rectangle.change_color(self.open_color)
        elif state == "close_list":
            self.rectangle.change_color(self.closed_color)
        elif state == "current":
            self.rectangle.change_color(self.current_color)
        else:
            self.rectangle.change_color(self.color)
