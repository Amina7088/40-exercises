#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    def swap_count(arr_sorted):
        index = {val: i for i, val in enumerate(arr)}
        visited = [False] * len(arr)
        swaps = 0

        for i in range(len(arr)):
            if visited[i] or arr[i] == arr_sorted[i]:
                continue

            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = index[arr_sorted[j]]
                cycle_size += 1
            swaps += cycle_size - 1
        return swaps

    return min(swap_count(sorted(arr)), swap_count(sorted(arr, reverse=True)))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
