class GridVisual(object):
    def __init__(self):
        self.cell_visuals = []        

    def add_cells(self, cells):
        self.cell_visuals = cells

    def draw(self, screen):
        for cell in self.cell_visuals:
            cell.draw(screen)

class Grid(object):
    def __init__(self, w, h)
        self.width = w
        self.height = h
        self.cells = []
        self.open_list = []
        self.closed_list = []
            