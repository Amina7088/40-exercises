#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    rows = len(grid)
    cols = len(grid[0])

    def detonate(grid):
        result = [['O'] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'O':
                    result[i][j] = '.'
                    if i > 0:
                        result[i-1][j] = '.'
                    if i < rows - 1:
                        result[i+1][j] = '.'
                    if j > 0:
                        result[i][j-1] = '.'
                    if j < cols - 1:
                        result[i][j+1] = '.'
        return [''.join(row) for row in result]

    if n == 1:
        return grid

    if n % 2 == 0:
        return ['O' * cols for _ in range(rows)]

    after3 = detonate(grid)

    if (n - 3) % 4 == 0:
        return after3

    after5 = detonate(after3)
    return after5


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
