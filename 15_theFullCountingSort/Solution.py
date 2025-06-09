#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    n = len(arr)
    
    buckets = [[] for _ in range(100)]

    for i in range(n):
        x = int(arr[i][0])
        s = arr[i][1]

        if i < n // 2:
            buckets[x].append('-') 
        else:
            buckets[x].append(s)

    print(' '.join(word for bucket in buckets for word in bucket))

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
