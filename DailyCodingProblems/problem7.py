# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

from collections import defaultdict
from time import time


def time_execution(f):
    def wrapper(*args, **kwargs):
        start_time = time()
        answer = f(*args, **kwargs)
        end_time = time()
        print('Execution took: {}'.format(end_time - start_time))
        return answer

    return wrapper


def _num_encodings_n_squared(s):
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
        total += _num_encodings_n_squared(s[2:])

    # Also recursively analyze as if we had chosen only the first digit + all the number
    # of ways the rest of the digits can be encoded
    total += _num_encodings_n_squared(s[1:])
    return total


def _num_encodings(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:].
    # e.g.: In cache[0] we store the # of ways to encode the string from 0 -> len(string).
    #       which is the answer

    # If defaultdict[key] does not exist it will call default_factory,
    # which for type "int" calls int() = 0
    cache = defaultdict(int)
    cache[len(s)] = 1  # Empty string is 1 valid encoding

    for i in reversed(range(len(s))):
        # Check if it starts with 0, because 0 has no encodings
        if s[i].startswith('0'):
            cache[i] = 0

        # If it's up to this point, the string len HAS to be equal to 1 and a
        # single digit only has 1 valid encoding.
        elif i == len(s) - 1:
            cache[i] = 1

        else:
            # check if the next 2 digits can be decoded together (less than 26)
            if int(s[i:i + 2]) <= 26:
                # if they are, they are a single option that can be paired with whatever comes next
                # (that is why +2)
                cache[i] = cache[i + 2]

            # also consider the single digit option and pair it with whatever comes 1 more after
            # this digit
            # It is "+=" because the num of encodings at this point is consider single and double digit usage
            cache[i] += cache[i + 1]

    return cache[0]


@time_execution
def num_encodings_n_squared(s):
    return _num_encodings_n_squared(s)


@time_execution
def num_encodings(s):
    return _num_encodings(s)


try:
    assert num_encodings('111') == 3
    print('Success!')

    # Test for speed
    q = '13411111122123321257231094561094567234613346134572310945612323094567223424346'
    print(num_encodings(q))
    print(num_encodings_n_squared(q))

except AssertionError:
    print('Failed!')
