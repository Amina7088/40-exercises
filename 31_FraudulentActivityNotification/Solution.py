#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure, d):
    notifications = 0
    window = sorted(expenditure[:d])

    for i in range(d, len(expenditure)):
        if d % 2 == 0:
            median = (window[d//2 - 1] + window[d//2]) / 2
        else:
            median = window[d//2]

        if expenditure[i] >= 2 * median:
            notifications += 1

        old = expenditure[i - d]
        del window[bisect.bisect_left(window, old)]
        bisect.insort(window, expenditure[i])

    return notifications
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
