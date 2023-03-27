#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    result = ""
    k = k % 26
    for i in range(len(s)):
        if s[i].isalpha():
            replacement = ord(s[i]) + k
            if s[i].islower() and replacement > ord('z'):
                replacement = replacement % ord('z') + ord('a') - 1
            if s[i].isupper() and replacement > ord('Z'):
                replacement = replacement % ord('Z')  + ord('A') - 1
            result += chr(replacement)
        else:
            result += s[i]
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
