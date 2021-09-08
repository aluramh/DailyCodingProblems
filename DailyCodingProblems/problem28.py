# This problem was asked by Palantir.

# Write an algorithm to justify text. Given a sequence of words and an integer
# line length k, return a list of strings which represents each line, fully
# justified.

# More specifically, you should have as many words as possible in each line.
# There should be at least one space between each word.
# Pad extra spaces when necessary so that each line has exactly length k.
# Spaces should be distributed as equally as possible, with the extra spaces,
# if any, distributed starting from the left.

# If you can only fit one word on a line, then you should pad the right-hand
# side with spaces.

# Each word is guaranteed not to be longer than k.

# For example, given the list of words:
# ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
# k = 16, you should return the following:

# ["the  quick brown", # 1 extra space on the left
# "fox  jumps  over", # 2 extra spaces distributed evenly
# "the   lazy   dog"] # 4 extra spaces distributed evenly

import math


def group_lines(words, max_size):
    """
    O(n)
    """
    lines = []
    current_line = []
    current_size = 0

    for word in words:
        # If the current line is empty, just add it.
        # The words always are less than size max_size
        if len(current_line) == 0:
            current_line.append(word)

        # Check if we can add this word to the line
        else:
            # with a "+1" because that is the minimum for a space
            word_size = len(word) + 1

            if max_size > (current_size + word_size):
                current_line.append(word)
                current_size += word_size

            # Else start a new line
            else:
                lines.append(current_line)
                current_line = [word]
                current_size = len(word)

    # Add the last item
    lines.append(current_line)

    return lines


def indent_line(line, k):
    """
    O(C)
    """
    min_spaces = len(line) - 1
    current_line_size = len("".join(line))

    spaces_to_allocate = k - current_line_size

    # Handle edge cases
    # There is only one word
    if len(line) == 1:
        # there are no spaces to allocate.
        if spaces_to_allocate == 0:
            return line[0]

        else:  # pad right hand side with all the spaces
            spaces = "".join(map(lambda x: " ", range(spaces_to_allocate)))
            return line[0] + spaces

        # Edge case: there are no spaces to allocate. len of word equals k
    if spaces_to_allocate == 0:
        # in this case, there can only be 1 item. return it.
        return line[0]

    # generate a string with equal spacing for each word
    equal_spacing_size = math.floor(spaces_to_allocate / min_spaces)
    equal_spaces = "".join(map(lambda x: " ", range(equal_spacing_size)))

    # allocate this value of extra spaces
    remnant_spaces = spaces_to_allocate % min_spaces

    # TODO: - Allocate all the remnant spaces
    index = 0
    while remnant_spaces > 0:
        # Reset the index if it is within limits of the line size
        if index == (len(line) - 1):
            index = 0

        line[index] += " "
        remnant_spaces -= 1
        index += 1

    # Finally merge the array into a string
    return equal_spaces.join(line)


def indent_lines(lines, k):
    result = []

    for line in lines:
        result.append(indent_line(line, k))

    return result


def group_and_indent(lines, k):
    """
    Runtime complexity: O(2n)
    """
    return indent_lines(group_lines(test, k), k)


try:
    # Initial test
    test = ["the", "quick", "brown", "fox",
            "jumps", "over", "the", "lazy", "dog"]
    k = 16
    answer = ["the  quick brown",  # 1 extra space on the left
              "fox  jumps  over",  # 2 extra spaces distributed evenly
              "the   lazy   dog"]  # 4 extra spaces distributed evenly
    result = indent_lines(group_lines(test, k), k)

    assert result == answer

    # Test #1
    test = ["alex", "vale", "sam"]
    k = 4
    answer = ["alex", "vale", "sam "]
    result = indent_lines(group_lines(test, k), k)

    assert result == answer

    print('Success!')

except AssertionError:
    print('Failed!')
