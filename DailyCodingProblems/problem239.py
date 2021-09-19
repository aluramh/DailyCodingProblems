# One way to unlock an Android phone is through a pattern of swipes across a
# 1-9 keypad.

# For a pattern to be valid, it must satisfy the following:

# All of its keys must be distinct.
# It must not connect two keys by jumping over a third key, unless that key
#  has already been used.
# For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

# Find the total number of valid unlock patterns of length N,
# where 1 <= N <= 9.

# keypad = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]


def swipe(start: int, end: int):
    start_index = start - 1
    end_index = end - 1

    # how many vertical?
    start_row = start // 3
    end_row = end // 3

    # how many horizontal?
    start_col = start_index % 3
    end_col = end_index % 3

    # return all I pass through
    passes_through = []
    while start_row != end_row or start_col != end_col:
        # Move the x-axis if needed
        if start_row < end_row:
            start_row += 1
        elif start_row > end_row:
            start_row -= 1

        # move the y-axis if needed
        if start_col < end_col:
            start_col += 1
        elif start_col > end_col:
            start_col -= 1

        # The next x,y is another digit that we passed through. Jot that down.
        next_index = (3 * start_row) + start_col
        passes_through.append(next_index + 1)

    return passes_through


def is_valid_pattern(pattern):
    memo = {}
    for i, key in enumerate(pattern):
        print(key)

        # If it's the first key, it's valid always, so save it in memo
        if i == 0:
            memo[key] = True

        # If key is not distinct, then it's invalid
        elif key in memo:
            return False

        else:
            # Check validity of key; that it is not passing through another key
            prev_key = pattern[i - 1]
            steps = swipe(prev_key, key)

            # all steps should be valid
            for step in steps:
                # Execute the step and save it in memo
                if step == key:
                    memo[key] = True

                # it is an intermediary step. check it has to be a number we
                # already went through. If not, return false
                elif step not in memo:
                    return False

    return True


tests = [
    ([1, 7], False),  # invalid cuz it goes to 4 and 4 hasn't been used
    ([4, 2, 2], False),
    ([4, 2, 1, 7], True),  # passes through 4
]

for (pattern, expected) in tests:
    r = is_valid_pattern(pattern)
    assert (r == expected)

print("Success!")
