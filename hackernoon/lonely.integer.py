#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    for i in range(len(a)):
        number = a[i]
        for j in range(i+1, len(a)):
            if a[j] == a[i]:
                a[i] = -a[i]
                a[j] = -a[j]
                break
    for i in range(len(a)):
        if a[i] > 0:
            return a[i]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
