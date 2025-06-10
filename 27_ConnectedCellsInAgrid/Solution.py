#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
def connectedCell(matrix):
    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]

    def dfs(r, c):
        if r < 0 or c < 0 or r >= m or c >= n:
            return 0
        if matrix[r][c] == 0 or visited[r][c]:
            return 0

        visited[r][c] = True
        size = 1
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]
        for dr, dc in directions:
            size += dfs(r + dr, c + dc)
        return size

    max_size = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and not visited[i][j]:
                max_size = max(max_size, dfs(i, j))

    return max_size

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
