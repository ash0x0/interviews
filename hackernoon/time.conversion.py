#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    result = ""
    if s[len(s)-2:] == "AM" and s[0:2] == "12":
        result += "00"
    elif s[len(s)-2:] == "PM" and s[0:2] == "12":
        result += "12"
    elif s[len(s)-2:] == "AM":
        result += s[0:2]
    elif s[len(s)-2:] == "PM":
        result += f"{12 + int(s[0:2])}"
    result += f":{s[3:5]}:{s[6:8]}"
    print(result)
    return f"{result}"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close() 
