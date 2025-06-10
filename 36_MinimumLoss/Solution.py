#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    n = len(price)
    prices_with_year = sorted([(p, i) for i, p in enumerate(price)])
    min_loss = 10**15
    for i in range(1, n):
        curr_price, curr_year = prices_with_year[i]
        prev_price, prev_year = prices_with_year[i-1]
        if prev_year > curr_year:
            loss = curr_price - prev_price
            if loss < min_loss:
                min_loss = loss
    return min_loss

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
