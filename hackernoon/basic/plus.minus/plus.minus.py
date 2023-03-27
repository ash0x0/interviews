#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count = len(arr)
    zero_count = 0
    positive_count = 0
    negative_count = 0
    for i in range(count):
        if arr[i] < 0:
            negative_count += 1
        if arr[i] == 0:
            zero_count += 1
        if arr[i] > 0:
            positive_count += 1
    print(f"{positive_count/count:.6f}\n{negative_count/count:.6f}\n{zero_count/count:.6f}")

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr) 
