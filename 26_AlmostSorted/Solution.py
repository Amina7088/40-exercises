#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    n = len(arr)
    sorted_arr = sorted(arr)

    if arr == sorted_arr:
        print("yes")
        return

    i = 0
    while i < n and arr[i] == sorted_arr[i]:
        i += 1

    j = n - 1
    while j >= 0 and arr[j] == sorted_arr[j]:
        j -= 1

    arr_swap = arr[:]
    arr_swap[i], arr_swap[j] = arr_swap[j], arr_swap[i]

    if arr_swap == sorted_arr:
        print("yes")
        print(f"swap {i+1} {j+1}")
        return

    arr_rev = arr[:]
    arr_rev[i:j+1] = arr_rev[i:j+1][::-1]

    if arr_rev == sorted_arr:
        print("yes")
        print(f"reverse {i+1} {j+1}")
        return

    print("no")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
