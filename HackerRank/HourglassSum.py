#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    """
    We'll use i and j to traverse and it will limit our values so we don't
    grab an out of bounds item
    """
    max_sum = None
    j = 0
    for i in range(4):
        for j in range(4):
            hourglass_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            hourglass_sum += arr[i + 1][j + 1]
            hourglass_sum += arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j +
                                                                            2]

            if max_sum is None or max_sum < hourglass_sum:
                max_sum = hourglass_sum

    print(max_sum)
    return max_sum
 

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
