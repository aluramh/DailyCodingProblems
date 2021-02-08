#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    """
    If walking from below 0 UP to 0, then it means we are exiting a valley.
    """
    D = 'D'
    U = 'U'

    # Always starts and ends with sea level
    level = 0
    valleys = 0

    # Count the altitude differential points
    for step in path:
        # Logic for executing the step itself
        if step == U:
            level += 1
            # If we are exiting from a deep; i.e. we were in a valley and are
            # not in sea-level after this step.
            if level == 0:
                valleys += 1
        elif step == D:
            level -= 1

    return valleys


if __name__ == '__main__':
    tests = [
        (12, 'DDUUDDUDUUUD', 2),
        (10, 'DUDDDUUDUU', 2),
        (8, 'UDDDUDUU', 1),
        (8, 'DDUUUUDD', 1),
    ]
    for (steps, path, expected_result) in tests:
        result = countingValleys(steps, path)
        print(result)
        assert result == expected_result
