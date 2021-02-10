#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c: List[int]):
    safe = 0
    jumps = 0
    cursor = 0

    while cursor < len(c) - 1:
        # Try to jump 2 ahead preferably
        if (cursor + 2) < len(c) and c[cursor + 2] == safe:
            cursor += 2
            jumps += 1

        elif (cursor + 1) < len(c) and c[cursor + 1] == safe:
            cursor += 1
            jumps += 1

    return jumps


print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
