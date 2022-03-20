#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_sum = 0
    max_sum = 0
    arr.sort()
    for i in range(0,4):
        min_sum += arr[i]
    for i in range(1, len(arr)):
        max_sum += arr[i]
    print(f"{min_sum} {max_sum}")
        
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr) 
