#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#

from collections import deque

def countLuck(matrix, k):
    n, m = len(matrix), len(matrix[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'M':
                start = (i, j)
            if matrix[i][j] == '*':
                goal = (i, j)

    visited = [[False]*m for _ in range(n)]
    queue = deque()
    queue.append((start[0], start[1], 0))  # x, y, fork_count
    visited[start[0]][start[1]] = True

    while queue:
        x, y, forks = queue.popleft()
        if (x, y) == goal:
            return "Impressed" if forks == k else "Oops!"

        neighbors = []
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and matrix[nx][ny] != 'X':
                    neighbors.append((nx, ny))

        if len(neighbors) > 1:
            forks += 1

        for nx, ny in neighbors:
            visited[nx][ny] = True
            queue.append((nx, ny, forks))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
