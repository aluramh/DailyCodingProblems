# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.


def num_encodings(s):
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
        total += num_encodings(s[2:])

    # Also recursively analyze as if we had chosen only the first digit + all the number
    # of ways the rest of the digits can be encoded
    total += num_encodings(s[1:])
    return total


try:
    assert num_encodings('111') == 3
    print('Success!')

    answer = num_encodings('134572310945672346')
    assert answer == 8

    print('Success!')

except AssertionError:
    print('Failed!')
