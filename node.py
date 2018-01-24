class Node(object):
    def __init__(self, pos):
        self.position = pos
        self.parent = None
        self.g_score = 0
        self.h_score = 0
        self.f_score = 0
        self.traversable = True
        self.is_goal = False
        self.is_start = False

    def change_state(self, state):
        if state == "start":
            self.is_start = not self.is_start
        if state == "goal":
            self.is_goal = not self.is_goal
        if state == "wall":
            self.traversable = not self.traversable

    def set_parent(self, node):
        if self.parent is None:
            self.parent = node
            return True
        else:
            temp_g = 10 if self.position[0] is node.position[0] or self.position[1] is node.position[1] else 14
            temp_g += node.g_score
            if temp_g < self.g_score:
                self.parent = node
                self.g_score = temp_g
            return False

    def calculate_g_score(self, node):
        if self.set_parent(node) is True:
            self.g_score = 10 if self.position[0] is node.position[0] or self.position[1] is node.position[1] else 14
            self.g_score += node.g_score
    
    def calculate_h_score(self, goal):
        self.h_score = 10 * (abs(goal.position[0] - self.position[0]) + abs(goal.position[1] - self.position[1]))
    
    def calculate_f_score(self):
        self.f_score = self.g_score + self.h_score