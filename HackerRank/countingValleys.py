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
    D = 'D'
    U = 'U'

    # Always starts and ends with sea level
    altitude_points = list(range(steps))
    altitude = 0

    # Count the altitude differential points
    for i, step in enumerate(path):
        # print(i, step, altitude)

        # Logic for executing the step itself
        if step == D:
            altitude -= 1
        elif step == U:
            altitude += 1

        altitude_points[i] = altitude

    # From 0 to 0; All that is between: If positive, it's a mountain. If negative, it's a valley.
    # Go through the altitude points again
    valleys = 0
    cursor = 0
    while cursor < len(altitude_points):
        altitude = altitude_points[cursor]

        if altitude < 0:
            # And continue until we are again at an altitude of 0
            while altitude != 0:
                cursor += 1
                altitude = altitude_points[cursor]

            valleys += 1
        else:
            cursor += 1

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
