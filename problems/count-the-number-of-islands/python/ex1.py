#!/usr/bin/python
 
import sys
import numpy as np
from io import StringIO   # StringIO behaves like a file object

class Solution:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.islands_map = np.loadtxt(self.path_to_file)

    def mark_current_island(self, matrix, x, y, r, c):
        if x<0 or x>=r or y<0 or y>=c or matrix[x][y] != 1:  # Boundary case for matrix
            return

        # Mark current cell as visited
        matrix[x][y] = 2

        # Make recursive call in all 8 adjacent directions
        self.mark_current_island(matrix,x+1,y,r,c)
        self.mark_current_island(matrix,x,y+1,r,c)
        self.mark_current_island(matrix,x-1,y,r,c)
        self.mark_current_island(matrix,x,y-1,r,c)

        self.mark_current_island(matrix,x-1,y-1,r,c)
        self.mark_current_island(matrix,x-1,y+1,r,c)
        self.mark_current_island(matrix,x+1,y-1,r,c)
        self.mark_current_island(matrix,x+1,y+1,r,c)


    def num_of_islands(self):
        # For FAST I/O
        # ...

        rows, cols = self.islands_map.shape
        # Empty matrix boundary case
        if rows == 0 :
            return 0
        no_of_islands = 0

        # Iterate for all cells of the array
        for i in range(rows):
            for j in range(cols):
                if self.islands_map[i][j]==1:
                    self.mark_current_island(self.islands_map,i,j,rows,cols)
                    no_of_islands += 1

        return no_of_islands


class ErrorsMessage:
    @staticmethod
    def print_line():
        return '*'*50

    @staticmethod
    def path_to_file_message():
        print(
            '''{0} \nPlease add path to the file, or print ./main.sh --help \n{1}'''.format(
            ErrorsMessage.print_line(),
            ErrorsMessage.print_line()
        ),
        file=sys.stderr
        )


    @staticmethod
    def help_message():
        print(
            '''{0} \nTo run the script please use the command bellow \n\t.\main.sh <path_to_the_file> \n{1}'''.format(
            ErrorsMessage.print_line(),
            ErrorsMessage.print_line()
        ),
        file=sys.stderr
        )


def main():
    # ...
    if (len(sys.argv) - 1) < 1:
        ErrorsMessage.path_to_file_message()
        return

    arg1 = sys.argv[1]

    if arg1 == '--help':
        ErrorsMessage.help_message()
        return

    if arg1 == '':
        ErrorsMessage.path_to_file_message()
        return

    # ...
    PATH_TO_FILE = arg1
    print(Solution(PATH_TO_FILE).num_of_islands(), file = sys.stdout)


if __name__ == "__main__":
    main()