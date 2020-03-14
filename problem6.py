# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

from collections import defaultdict


def num_encodings_n_squared(s):
    # If it starts with 0 it is not encodable
    if s.startswith('0'):
        return 0

    # If the length of the number is less than 1, return "1".
    # This is because empty string or single digit only has 1 possible way of encoding.
    elif len(s) <= 1:
        return 1

    total = 0

    # check if the first 2 digits are less than 26. Then pair this + all the number of
    # ways the rest of the digits can be encoded
    if int(s[:2]) <= 26:
        total += num_encodings_n_squared(s[2:])

    # Also recursively analyze as if we had chosen only the first digit + all the number
    # of ways the rest of the digits can be encoded
    total += num_encodings_n_squared(s[1:])
    return total


def num_encodings(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:].
    # e.g.: In cache[0] we store the # of ways to encode the string from 0 -> len(string).
    #       which is the answer

    # If defaultdict[key] does not exist it will call default_factory,
    # which for type "int" calls int() = 0
    cache = defaultdict(int)
    cache[len(s)] = 1  # Empty string is 1 valid encoding

    for i in reversed(range(len(s))):
        print(i)
        # Check if it starts with 0, because 0 has no encodings
        if s[i].startswith('0'):
            return 0  # (go to next loop)

        # Check if it's a single digit
        # (go to next loop)
        elif i == len(s) - 1:
            cache[i] = 1

        else:
            # If 2 digits are less than 26 (can use 2 digits + whatever comes next)
            if int(s[i:i + 2]) <= 26:
                cache[i] = cache[i + 2]

            # sum these previous 2 and store in cache
            cache[i] += cache[i + 1]

    return cache[0]


try:
    assert num_encodings('111') == 3
    print('Success!')

    answer = num_encodings_n_squared('134572310945672346')
    assert answer == 8

    print('Success!')

except AssertionError:
    print('Failed!')
