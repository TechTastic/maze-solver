import unittest
import random

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        for i in range(100):
            num_cols = random.randint(1, 50)
            num_rows = random.randint(1, 50)
            print(f"Testing Maze with {num_cols} columns and {num_rows} rows...")
            cell_size_x = random.randint(1, 10)
            cell_size_y = random.randint(1, 10)
            print(f"Cell Sizes are {cell_size_x} and {cell_size_y}...")
            m1 = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)
            self.assertEqual(
                len(m1._cells),
                num_cols,
            )
            self.assertEqual(
                len(m1._cells[0]),
                num_rows,
            )

if __name__ == "__main__":
    unittest.main()