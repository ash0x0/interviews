#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def makePlayerMove(player_num, towers):
    solution_found = False
    for i in range(len(towers)):
        for j in range(towers[i], 1, -1):
            if towers[i] % j == 0:
                towers[i] = int(towers[i] / j)
                solution_found = True
                break
        if solution_found:
            return None
    if not solution_found:
        if player_num == 1:
            return 2
        else:
            return 1


def towerBreakers(n, m):
    # Write your code here
    towers = n * [m]
    while (True):
        for i in range(1, 3):
            move_result = makePlayerMove(i, towers)
            if move_result != None:
                return move_result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
 
