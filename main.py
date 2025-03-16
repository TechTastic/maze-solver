from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    print("Hello?")
    win = Window(800, 600)

    #cell = Cell(win)
    #cell.draw(200, 200, 400, 400)
    #cell2 = Cell(win)
    #cell2.draw(400, 400, 600, 600)
    #cell.draw_move(cell2, undo=True)

    maze = Maze(25, 25, 25, 35, 20, 20, win)
    maze.solve()

    win.wait_for_close()

main()