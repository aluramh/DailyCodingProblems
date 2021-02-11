# Complete the repeatedString function below.
def repeatedString(s, n):
    # Handle edge cases
    if len(s) == 0:
        return 0
    if len(s) == 1 and s == 'a':
        return n

    a = "a"

    # Count in original str
    count_per_repetition = 0
    for char in s:
        if char == a:
            count_per_repetition += 1

    # Multiply by the times the entire string fits in the n characters
    repeats_entirely = n // len(s)
    count = repeats_entirely * count_per_repetition

    # Handle the remainder
    remainder_substr_len = n % len(s)

    substr = s[0:remainder_substr_len]
    for char in substr:
        if char == a:
            count += 1

    return count


tests = [
    # ('aba', 10, 7), ('a', 1000000000000, 1000000000000),
    # NOTE: - MISSING 5 OCCURRENCES
    (
        'ojowrdcpavatfacuunxycyrmpbkvaxyrsgquwehhurnicgicmrpmgegftjszgvsgqavcrvdtsxlkxjpqtlnkjuyraknwxmnthfpt',
        685118368975,
        41107102139,
    )
]

for s, n, expected_result in tests:
    r = repeatedString(s, n)
    print(r)
    assert r == expected_result
