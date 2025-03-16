import time
import random

from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None, wall_color="black", path_color="red", undo_color="gray"):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed != None:
            random.seed(seed)
        
        self.wall_color = wall_color
        self.path_color = path_color
        self.undo_color = undo_color

        self._cells = []

        log_maze_gen_start = f"Generating {self.num_cols}x{self.num_rows} Maze of {self.cell_size_x}x{self.cell_size_y} cells with a margin of {x1}, {y1}"
        if seed:
            log_maze_gen_start += f"with seed {self.seed}"
        print(log_maze_gen_start + "...")
        self._create_cells()
        self._break_entrance_and_exit()
        print("Randomizing Walls...")
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
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

        if self.win:
            self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2, self.wall_color, self.win.bg_color)
        else:
            self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2, self.wall_color)
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
        self._cells[i][j].visited = True

        while True:
            possible_directions = []
            if 0 <= (i - 1) < len(self._cells):
                possible_directions.append((i - 1, j))
            if 0 <= (i + 1) < len(self._cells):
                possible_directions.append((i + 1, j))
            if 0 <= (j - 1) < len(self._cells[i]):
                possible_directions.append((i, j - 1))
            if 0 <= (j + 1) < len(self._cells[i]):
                possible_directions.append((i, j + 1))
            possible_directions = list(filter(lambda tup: not self._cells[tup[0]][tup[1]].visited, possible_directions))

            if not possible_directions:
                self._draw_cell(i, j)
                return
            
            random_index = random.randrange(0, len(possible_directions))
            x, y = possible_directions[random_index]

            if i > x:
                self._cells[i][j].has_left_wall = False
                self._cells[x][y].has_right_wall = False
            if i < x:
                self._cells[i][j].has_right_wall = False
                self._cells[x][y].has_left_wall = False
            if j > y:
                self._cells[i][j].has_top_wall = False
                self._cells[x][y].has_bottom_wall = False
            if j < y:
                self._cells[i][j].has_bottom_wall = False
                self._cells[x][y].has_top_wall = False
            
            self._break_walls_r(x, y)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == len(self._cells) - 1 and j == len(self._cells[i]) - 1:
            return True
        
        possible_directions = []
        if 0 <= (i - 1) < len(self._cells):
            possible_directions.append((i - 1, j))
        if 0 <= (i + 1) < len(self._cells):
            possible_directions.append((i + 1, j))
        if 0 <= (j - 1) < len(self._cells[i]):
            possible_directions.append((i, j - 1))
        if 0 <= (j + 1) < len(self._cells[i]):
            possible_directions.append((i, j + 1))
        
        for direction in possible_directions:
            x, y = direction

            has_wall = False
            if i > x:
                has_wall = self._cells[i][j].has_left_wall
            if i < x:
                has_wall = self._cells[i][j].has_right_wall
            if j > y:
                has_wall = self._cells[i][j].has_top_wall
            if j < y:
                has_wall = self._cells[i][j].has_bottom_wall
            
            if not has_wall and not self._cells[x][y].visited:
                self._cells[i][j].draw_move(self._cells[x][y], self.path_color, self.undo_color)
                if self._solve_r(x, y):
                    return True
                self._cells[i][j].draw_move(self._cells[x][y], undo=True)
        
        return False