#!/bin/python3

import math
import os
import random
import re
import sys

def rotate_matrix(matrix, r):
    m, n = len(matrix), len(matrix[0])
    result = [[0] * n for _ in range(m)]
    layers = min(m, n) // 2

    for layer in range(layers):
        elements = []

        for i in range(layer, n - layer):
            elements.append(matrix[layer][i])
        for i in range(layer + 1, m - layer - 1):
            elements.append(matrix[i][n - layer - 1])
        for i in range(n - layer - 1, layer - 1, -1):
            elements.append(matrix[m - layer - 1][i])
        for i in range(m - layer - 2, layer, -1):
            elements.append(matrix[i][layer])

        rotation = r % len(elements)
        rotated = elements[rotation:] + elements[:rotation]

        idx = 0
        for i in range(layer, n - layer):
            result[layer][i] = rotated[idx]
            idx += 1
        for i in range(layer + 1, m - layer - 1):
            result[i][n - layer - 1] = rotated[idx]
            idx += 1
        for i in range(n - layer - 1, layer - 1, -1):
            result[m - layer - 1][i] = rotated[idx]
            idx += 1
        for i in range(m - layer - 2, layer, -1):
            result[i][layer] = rotated[idx]
            idx += 1

    return result

def matrixRotation(matrix, r):
    rotated = rotate_matrix(matrix, r)
    for row in rotated:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    r = int(first_multiple_input[2])

    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
