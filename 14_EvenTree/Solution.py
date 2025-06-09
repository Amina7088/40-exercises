#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    from collections import defaultdict

    graph = defaultdict(list)
    for u, v in zip(t_from, t_to):
        graph[u].append(v)
        graph[v].append(u)

    result = 0

    def depth(node, parent):
        nonlocal result
        size = 1 

        for neighbor in graph[node]:
            if neighbor != parent:
                subtree_size = depth(neighbor, node)
                if subtree_size % 2 == 0:
                    result += 1 
                else:
                    size += subtree_size
        return size

    depth(1, -1) 
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t_nodes, t_edges = map(int, input().rstrip().split())

    t_from = [0] * t_edges
    t_to = [0] * t_edges

    for i in range(t_edges):
        t_from[i], t_to[i] = map(int, input().rstrip().split())

    res = evenForest(t_nodes, t_edges, t_from, t_to)

    fptr.write(str(res) + '\n')

    fptr.close()
