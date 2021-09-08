# This is your coding interview problem for today.

# This problem was asked by Amazon.

# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single
# count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A 3B 2C 1D 2A".

# Implement run-length encoding and decoding.
# You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
# You can assume the string to be decoded is valid.


def decode(chars):
    final = ''
    cumulative = 0

    for i in enumerate(chars):
        # Empty cumulative. Start a new one.
        if (cumulative == 0):
            cumulative += 1

        else:
            if chars[i] == chars[i - 1]:
                cumulative += 1
            else:
                final += '{}{}'.format(cumulative, chars[i - 1])
                cumulative = 1

    # Handle final item
    size = len(chars)
    final += '{}{}'.format(cumulative, chars[size - 1])

    return final


try:
    assert decode('AAAABBBCCDAA') == '4A3B2C1D2A'
    print('Success!')

    assert decode('AAAABBBCCDAAZ') == '4A3B2C1D2A1Z'
    print('Success!')

    # INVALID CASE
    # assert decode('') == ''
    # print('Success!')

except AssertionError:
    print('Failed!')
