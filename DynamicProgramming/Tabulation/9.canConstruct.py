import numpy
from numpy.core.numeric import Infinity


def can_construct(target, A):
    string_length = len(target) + 1
    matrix = numpy.zeros(string_length, dtype=bool)
    matrix[0] = True

    for i in range(string_length):
        if matrix[i] == True:
            for x in A:
                index = i + len(x)
                substring = target[i:index]

                if (index < string_length) and (x == substring):
                    matrix[index] = True

    return matrix[len(target)]


def count_construct(target, A):
    string_length = len(target) + 1
    matrix = numpy.zeros(string_length, dtype=int)
    matrix[0] = 1

    for cursor in range(string_length):
        if matrix[cursor] is not None:
            for word in A:
                index_plus_word = cursor + len(word)
                substring = target[cursor:index_plus_word]

                if index_plus_word < string_length and substring == word:
                    # The value to store in the tabulation is the value of the
                    # cursor, plus the number of ways for the position that
                    # comes at the index+word.
                    matrix[index_plus_word] = matrix[cursor] + matrix[
                        index_plus_word]

    return matrix[len(target)]


def how_construct(target, A):
    string_length = len(target) + 1
    matrix = list(map(lambda x: None, range(string_length)))
    matrix[0] = []

    for cursor in range(string_length):
        # If there is a value in this spot, execute this logic
        if matrix[cursor] is not None:
            for word in A:
                index_with_word = cursor + len(word)
                # Create a substring from the current size, up to the length of the word.
                # This is to see if this string can be accomodated inside the target.
                substring = target[cursor:index_with_word]

                if index_with_word < string_length and substring == word:
                    matrix[index_with_word] = matrix[cursor] + [word]

    return matrix[len(target)]


def all_construct(target, A):
    string_length = len(target) + 1
    matrix = list(map(lambda x: [], range(string_length)))
    matrix[0] = [[]]

    for cursor in range(string_length):
        # If there is a value in this spot, execute this logic
        if matrix[cursor] is not None:
            for word in A:
                index_with_word = cursor + len(word)
                # Create a substring from the current size, up to the length of the word.
                # This is to see if this string can be accomodated inside the target.
                substring = target[cursor:index_with_word]

                if index_with_word < string_length and substring == word:
                    if len(matrix[cursor]) != 0:
                        # Iterate through the already available options and
                        # concatenate this word as a possible option to get
                        # to this point.
                        options = list(
                            map(
                                lambda option: option + [word],
                                matrix[cursor],
                            ))

                        # Concatenate these arrays together
                        matrix[index_with_word] = matrix[
                            index_with_word] + options
                    else:
                        matrix[index_with_word] = [[word]]

    return matrix[len(target)]


def best_construct(target, A):
    options = all_construct(target, A)
    answer = None
    min_len = -1

    for option in options:
        option_length = len(option)

        if (answer is None) or (option_length < min_len):
            answer = option
            min_len = option_length

    return answer


tests = [('abcdef', ['ab', 'abc', 'cd', 'def', 'e', 'f', 'abcd']),
         ('purple', ['purp', 'p', 'ur', 'le', 'purpl']),
         ('cat', ['cat', 'c', 'at', 'dog']), ('', ['alex']),
         ('alex', ['al', 'lex', 'ale', 'a', 'alex']),
         ('aaaaaaaaaaaaaaaaaaaaaz', ['a', 'aa', 'aaa', 'aaaa'])]

for target, A in tests:
    print("Target:", target)

    r = can_construct(target, A)
    print("can_construct:", r)

    r = count_construct(target, A)
    print("count_construct:", r)

    r = how_construct(target, A)
    print("how_construct:", r)

    r = all_construct(target, A)
    print("all_construct:", r)

    r = best_construct(target, A)
    print("best_construct:", r)

    print()
