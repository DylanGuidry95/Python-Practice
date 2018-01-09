import sys, pygame

class CellVisual(object):
    '''Visual representation of the cell in the screen space'''
    def __init__(self, cell, dim, col):
        self.size = dim
        self.position = cell.position
        self.color = col
        self.surface = pygame.Surface((self.size[0], self.size[1]))
        self.cellInfo = cell
    def draw(self, screen):
        '''draws the cell to the screen'''
        pygame.draw.rect(screen, self.color,
                         (self.position[0], self.position[1], self.size[0], self.size[1]))
    def change_color(self, col):
        '''Changes the color of the cell'''
        self.color = col    

class Cell(object):
    def __init__(self, pos):
        self.f_score = 0
        self.h_score = 0
        self.g_score = 0
        self.position = pos
        self.parent = None
    def calculate_g_score(self, cell):
        '''Calcualtes the g score of the cell based on the direction it is from the current cell'''
        if cell.position[0] == self.position[0] or cell.position[1] == self.position[1]:
            self.g_score = 10
        else:
            self.g_score = 14
    def calculate_h_score(self, goal):
        '''Calculates the h score of the cell'''
        self.h_score = 10 * (abs(self.position[0] - goal.position[0]) +
                             abs(self.position[1] - goal.position[1]))
    def calculate_f_score(self):
        '''Calculate the f score of the cell'''
        self.f_score = self.g_score + self.h_score
    def set_parent(self, cell):
        if self.parent is None:
            self.parent = cell
                if self.position[0] != cell.position[0] && self.position[0] != cell.position[0]
                    self.g_score = cell.g_score + 14
                else:
                    self.g_score = cell.g_score + 10
        else:
            newg = 0
            if self.position[0] != cell.position[0] && self.position[0] != cell.position[0]
                newg = cell.g_score + 14
            else:
                newg = cell.g_score + 10
            if newg > self.g_score:
                self.g_score = newg
                self.parent = cell
            
