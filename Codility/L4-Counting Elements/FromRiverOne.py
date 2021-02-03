# 1h 39m

# Task description
# Task 1

# Python
# C
# C++
# C#
# Go
# Java 8
# Java 11
# JavaScript
# Kotlin
# Lua
# Objective-C
# Pascal
# PHP
# Perl
# Python
# Ruby
# Scala
# Swift 4
# Visual Basic
# A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

# You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

# The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

# For example, you are given integer X = 5 and array A such that:

#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

# Write a function:

# def solution(X, A)

# that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

# If the frog is never able to jump to the other side of the river, the function should return −1.

# For example, given X = 5 and array A such that:

#   A[0] = 1
#   A[1] = 3
#   A[2] = 1
#   A[3] = 4
#   A[4] = 2
#   A[5] = 3
#   A[6] = 5
#   A[7] = 4
# the function should return 6, as explained above.

# Write an efficient algorithm for the following assumptions:

# N and X are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..X].
# Copyright 2009–2021 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
# Solution
# Files
# task1

# solution.py

# test-input.txt

# solution.py
# 12346789510
# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")


def solution(X, A):
    count_array = [0] * (X + 1)
    count_array[0] = 1  # his triggers the first step
    cursor = 0

    for time, pos in enumerate(A):
        # Increase the counter on the counts array
        count_array[pos] += 1

        # Move the cursor if possible to the next empty spot on the right
        while count_array[cursor] != 0:
            cursor += 1

            # If the cursor's landing spot is greater than the target X, then
            # this is the end, so return the time that this happened as the
            # result.
            if cursor > X:
                return time

    return -1


if __name__ == "__main__":
    try:
        tests = [
            (5, [1, 3, 1, 4, 2, 3, 5, 4], 6),
            (5, [1, 3, 1, 4, 2, 3, 4], -1),
            (5, [1, 3, 1, 4, 3, 5, 4], -1),
        ]

        for X, A, expected_result in tests:
            result = solution(X, A)
            print(result)
            assert result == expected_result

    except AssertionError as e:
        print("AssertionError", e)
