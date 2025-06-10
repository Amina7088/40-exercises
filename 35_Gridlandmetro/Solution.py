#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

def gridlandMetro(n, m, k, tracks):
    occupied = {}
    for r, c1, c2 in tracks:
        if r not in occupied:
            occupied[r] = []
        occupied[r].append((c1, c2))
    
    total = n * m
    for r in occupied:
        occupied[r].sort()
        merged = []
        start, end = occupied[r][0]
        for i in range(1, len(occupied[r])):
            c1, c2 = occupied[r][i]
            if c1 <= end + 1:
                end = max(end, c2)
            else:
                merged.append((start, end))
                start, end = c1, c2
        merged.append((start, end))

        for c1, c2 in merged:
            total -= (c2 - c1 + 1)
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
