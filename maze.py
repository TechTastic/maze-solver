import time
import random

from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed != None:
            random.seed(seed)

        self._cells = []

        self._create_cells()
    
    def _create_cells(self):
        columns = []
        for col in range(self.num_cols):
            rows = []
            for row in range(self.num_rows):
                rows.append(Cell(self.win))
            columns.append(rows)
        
        self._cells = columns

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    
    def _draw_cell(self, i, j):
        cell_x1 = self.x1 + (i * self.cell_size_x)
        cell_y1 = self.y1 + (j * self.cell_size_y)
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y2 = cell_y1 + self.cell_size_y

        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)
        self._animate()
    
    def _animate(self):
        if not self.win:
            return
        self.win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        topmost_cell = self._cells[0][0]
        topmost_cell.has_top_wall = False
        self._draw_cell(0, 0)

        bottommost_cell = self._cells[self.num_cols - 1][self.num_rows - 1]
        bottommost_cell.has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
    
    def _break_walls_r(self, i, j):
        print(f"_break_walls_r called for cell ({i}, {j})")
        print(f"Maze dimensions: {len(self._cells)} rows, {len(self._cells[i])} columns")
        if self._cells[i][j].visited:
            return
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            possible_directions = []
            if i - 1 >= 0 and not self._cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))
            if i + 1 < len(self._cells) and not self._cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))
            if j - 1 >= 0 and not self._cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))
            if j + 1 < len(self._cells[i]) and not self._cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))
            
            print("Possible Directions: ", possible_directions)
            
            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
            
            direction = random.randrange(0, len(possible_directions))
            print("Randon Direction: ", possible_directions[direction])
            x, y = possible_directions[direction]
            next_cell = self._cells[x][y]
            print(f"Breaking wall between ({i}, {j}) and ({x}, {y})")
            if i > 0 and x == i - 1:  # Moving up
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif i < len(self._cells) - 1 and x == i + 1:  # Moving down
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            elif y > 0 and y == j - 1:  # Moving left
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif y < len(self._cells[i]) - 1 and y == j + 1:  # Moving right
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            
            self._draw_cell(i, j)
            self._draw_cell(x, y)

            self._break_walls_r(x, y)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
    
    def solve(self):
        pass