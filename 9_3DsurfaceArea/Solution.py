#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

def surfaceArea(A):
    n = len(A)
    m = len(A[0])
    total = 0

    for i in range(n):
        for j in range(m):
            if A[i][j] > 0:
                total += 
                total += max(A[i][j] - A[i-1][j], 0) if i > 0 else A[i][j]
                total += max(A[i][j] - A[i+1][j], 0) if i < n-1 else A[i][j]
                total += max(A[i][j] - A[i][j-1], 0) if j > 0 else A[i][j]
                total += max(A[i][j] - A[i][j+1], 0) if j < m-1 else A[i][j]
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
