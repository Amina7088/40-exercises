#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

from collections import defaultdict

def journeyToMoon(n, astronaut):
    graph = defaultdict(list)
    for u, v in astronaut:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    
    def dfs(node):
        stack = [node]
        size = 0
        while stack:
            curr = stack.pop()
            if not visited[curr]:
                visited[curr] = True
                size += 1
                for neighbor in graph[curr]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return size

    groups = []
    
    for i in range(n):
        if not visited[i]:
            group_size = dfs(i)
            groups.append(group_size)
    
    total_pairs = 0
    sum_so_far = 0
    
    for size in groups:
        total_pairs += sum_so_far * size
        sum_so_far += size
    
    return total_pairs
   # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
