import sys
import argparse
from enum import Enum

from window import Window
from maze import Maze, Algorithm

parser = argparse.ArgumentParser(description="Maze Generation and Solving")
parser.add_argument("--margin", type=int, default=20, help="sets the padding between the top-left corner of the screen and the top-left corner of the maze, defaults to 20")
parser.add_argument("--rows", type=int, default=28, help="sets the number of rows in the maze, defaults to 28")
parser.add_argument("--columns", type=int, default=38, help="sets the number of columns in the maze, defaults to 38")
parser.add_argument("--cell-size", type=int, default=20, help="sets the size of every cell, defaults to 20")
parser.add_argument("--seed", type=int, help="an initial input seed for the random package")
parser.add_argument("--bg-color", default="white", help="sets the background color of the window, defaults to white")
parser.add_argument("--wall-color", default="black", help="sets the color of the walls in the maze, defaults to black")
parser.add_argument("--path-color", default="red", help="sets the color of the solution path when solving the maze, defaults to red")
parser.add_argument("--undo-color", default="gray", help="sets the color of the solution path when it backtracks while solving the maze, defaults to gray")
parser.add_argument("--animation-speed", type=float, default=0.05, help="sets the sleep timer used to simulate animation")
parser.add_argument("--start-position-x", type=int, default=0, help="sets the starting x position for the maze, has to be on the edge")
parser.add_argument("--start-position-y", type=int, default=0, help="sets the starting y position for the maze, has to be on the edge")
parser.add_argument("--end-position-x", type=int, default=None, help="sets the ending x position for the maze, has to be on the edge")
parser.add_argument("--end-position-y", type=int, default=None, help="sets the ending y position for the maze, has to be on the edge")
parser.add_argument("--algorithm", type=Algorithm, default=Algorithm.DFS, help="")

def main():
    args = parser.parse_args()

    margin = args.margin
    rows = args.rows
    columns = args.columns
    cell_size = args.cell_size
    seed = args.seed
    bg_color = args.bg_color
    wall_color = args.wall_color
    path_color = args.path_color
    undo_color = args.undo_color
    animation_speed = args.animation_speed
    start_x = args.start_position_x
    start_y = args.start_position_y
    end_x = args.end_position_x
    end_y = args.end_position_y
    algorithm = args.algorithm

    max_recursion_level = rows * columns
    if max_recursion_level > sys.getrecursionlimit():
        print(f"{max_recursion_level} ({rows} * {columns}) recursive depth is greater than {sys.getrecursionlimit()} (default recursion limit)!")
        print(f"Setting new recursion limit to {max_recursion_level}...")
        print()
        sys.setrecursionlimit(max_recursion_level)

    win = Window(800, 600, bg_color)
    maze = Maze(margin, margin, rows, columns, cell_size, cell_size, win, seed, wall_color, path_color, undo_color, animation_speed, start_x, start_y, end_x, end_y, algorithm)
    print("Solving...")
    maze.solve()
    print("Solved!")

    win.wait_for_close()

main()