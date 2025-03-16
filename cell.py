from point import Point
from line import Line

class Cell:
    def __init__(self, win=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        if not self._win:
            return

        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        a = Point(self._x1, self._y1)
        b = Point(self._x1, self._y2)
        c = Point(self._x2, self._y2)
        d = Point(self._x2, self._y1)

        if self.has_left_wall:
            self._win.draw_line(Line(a, b), "black")
        else:
            self._win.draw_line(Line(a, b), "white")
        if self.has_bottom_wall:
            self._win.draw_line(Line(b, c), "black")
        else:
            self._win.draw_line(Line(b, c), "white")
        if self.has_right_wall:
            self._win.draw_line(Line(c, d), "black")
        else:
            self._win.draw_line(Line(c, d), "white")
        if self.has_top_wall:
            self._win.draw_line(Line(d, a), "black")
        else:
            self._win.draw_line(Line(d, a), "white")
    
    def draw_move(self, to_cell, undo=False):
        if not self._win:
            return

        a = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        b = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)

        fill_color = "red"
        if undo:
            fill_color = "gray"
        
        self._win.draw_line(Line(a, b), fill_color)
            