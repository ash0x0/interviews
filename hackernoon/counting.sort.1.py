#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    frequency_arr = [0] * 100
    sorted_arr = []
    for i in range(len(arr)):
        frequency_arr[arr[i]] += 1
    # for i in range(len(frequency_arr)):
    #     if frequency_arr[i] < 1:
    #         continue
    #     sorted_arr.extend([i] * frequency_arr[i])
    return frequency_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
