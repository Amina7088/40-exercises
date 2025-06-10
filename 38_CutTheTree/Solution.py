#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#

import sys
sys.setrecursionlimit(10**7)

def cutTheTree(data, edges):
    n = len(data)
    tree = [[] for _ in range(n)]
    for u, v in edges:
        tree[u-1].append(v-1)
        tree[v-1].append(u-1)

    total_sum = sum(data)
    min_diff = total_sum

    visited = [False]*n

    def dfs(node):
        visited[node] = True
        subtree_sum = data[node]
        for nei in tree[node]:
            if not visited[nei]:
                subtree_sum += dfs(nei)
        nonlocal min_diff
        diff = abs(total_sum - 2*subtree_sum)
        if diff < min_diff:
            min_diff = diff
        return subtree_sum

    dfs(0)
    return min_diff
   # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
