''' File: node.py
    Author: Dylan Guidry
    Date: 1/24/2018'''
class Node(object):
    '''Class that will be used to create node objects. These objects
    will be used in the path finding algorithm known as A_Star'''
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
        '''Changes the value of the state specified with the value of state
        passed in. If the state was currently true on funciton call it will
        be set to false'''
        if state == "start":
            self.is_start = not self.is_start
        if state == "goal":
            self.is_goal = not self.is_goal
        if state == "wall":
            self.traversable = not self.traversable

    def set_parent(self, node):
        '''Attempts to change the value of the parent variable. If the value is
        None the parent is automaticly set to the value of node passed in. Otherwise
        a new G score is calcualted and if it is cheaper than the current the parent
        is changed to the node passed in and the G score is modified to reflect the
        change in parents'''
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
        '''Calculates the movement cost to move from nodes parent to it self. If the
        movement is horizontal or vertical the cost is parent's G score + 10. If the
        movement is diagonal the cost is parent's G score + 14'''
        if self.set_parent(node) is True:
            self.g_score = 10 if self.position[0] is node.position[0] or self.position[1] is node.position[1] else 14
            self.g_score += node.g_score
    
    def calculate_h_score(self, goal):
        '''Calculates the estimated movement cost to move from this node to the goal.'''
        self.h_score = 10 * (abs(goal.position[0] - self.position[0]) + abs(goal.position[1] - self.position[1]))
    
    def calculate_f_score(self):
        '''Calculates the fscore which is the sum of the H score and G score of the node'''
        self.f_score = self.g_score + self.h_score