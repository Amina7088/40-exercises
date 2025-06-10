#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

MOD = 10**9 + 7
MAX = 100001

fact = [1] * MAX
inv_fact = [1] * MAX

for i in range(1, MAX):
    fact[i] = (fact[i - 1] * i) % MOD

inv_fact[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
for i in range(MAX - 2, -1, -1):
    inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

freq = []

def initialize(s):
    n = len(s)
    global freq
    freq = [[0] * 26 for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(26):
            freq[i][j] = freq[i - 1][j]
        freq[i][ord(s[i - 1]) - ord('a')] += 1

def answerQuery(l, r):
    count = [freq[r][i] - freq[l - 1][i] for i in range(26)]
    odd = sum(c % 2 for c in count)
    half = sum(c // 2 for c in count)

    res = fact[half]
    for c in count:
        res = (res * inv_fact[c // 2]) % MOD
    if odd == 0:
        return res
    return (res * odd) % MOD
   # Return the answer for this query modulo 1000000007.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
