#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    left_sum = 0
    right_sum = 0
    # looping over rows
    for i in range(len(arr)):
        # looping each row
        for j in range(len(arr[i])):
            if i == j:
                left_sum += arr[i][j]
            if i == len(arr[i]) - 1 - j:
                right_sum += arr[i][j]
    return abs(left_sum - right_sum)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
