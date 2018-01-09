from cell import Cell

class GridVisual(object):
    def __init__(self):
        self.cell_visuals = []        

    def add_cells(self, cells):
        self.cell_visuals = cells

    def draw(self, screen):
        for cell in self.cell_visuals:
            cell.draw(screen)    

class Grid(object):
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.cells = []
        self.open_list = []
        self.closed_list = []
        self.num_cells = 0
        self.start_cell = None
        self.goal_cell = None
    def create_cells(self):        
        for x in range(0, self.width):
            for y in range(0, self.height):
                 self.cells[self.num_cells] = Cell((x,y))
                 self.num_cells += 1
    def set_start(self, pos):
        for cell in self.cells:
            if cell.position[0] == pos[0] and cell.position[1] == pos[1]:
                self.start_cell = cell
    def set_goal(self, pos):
        for cell in self.cells:
            if cell.position[0] == pos[0] and cell.position[1] == pos[1]:
                self.goal_cell = cell
    def get_neighbors(self, cell):
        neighbor_pos = ((1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1))
        neighbor = []
        for cell in self.cells:
            for pos in neighbor_pos:
                if cell.position[0] == pos[0] and cell.position[1] == pos[1]
                    neighbor.append(cell)
        return neighbor
            