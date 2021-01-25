def all_construct_RECURSIVE(target, wordbank):
    if target == '':
        return 1

    # This is separate for each stackcall
    total_count = 0

    # We want to loop through EVERY word ALWAYS to see how many can build the target
    for word in wordbank:
        # Check if the current word is a prefix of the target
        if target.find(word) == 0:
            # Remove the prefix from the string to create a new target
            new_target = target[target.index(word) + len(word):len(target)]
            num_ways_rest = all_construct_RECURSIVE(new_target, wordbank)

            total_count += num_ways_rest

    return total_count


def all_construct(target, wordbank, memo):
    if target in dict.keys(memo):
        return memo[target]

    if target == '':
        return [[]]

    # This is separate for each stackcall
    result = []

    # We want to loop through EVERY word ALWAYS to see how many can build the target
    for word in wordbank:
        # Check if the current word is a prefix of the target
        if target.find(word) == 0:
            # Remove the prefix from the string to create a new target
            suffix = target[target.index(word) + len(word):len(target)]

            # Returns an array of all the ways to build the suffix
            suffix_ways = all_construct(suffix, wordbank, memo)

            # Get the target ways. For each way, append the current word iteration
            target_ways = list(map(lambda way: [word] + way, suffix_ways))

            # Return the result
            result += target_ways

    memo[target] = result
    return memo[target]


if __name__ == "__main__":
    try:
        print(all_construct(
            "skateboard",
            ['skate', "board"],
            {},
        ))

        print(
            all_construct(
                "enterapotentpot",
                ['a', "p", "ent", "enter", "ot", "o", "t"],
                {},
            ))

        print(all_construct(
            "purple",
            ['purp', "p", "ur", "le", "purpl"],
            {},
        ))

        print(
            all_construct("eeeeeeeeeeeee", [
                'e',
                "ee",
                "eee",
                "eeee",
                "eeeee",
                "eeeeee",
                "eeeeeee",
                "eeeeeeee",
            ], {}))
    except Exception as e:
        print(e)
