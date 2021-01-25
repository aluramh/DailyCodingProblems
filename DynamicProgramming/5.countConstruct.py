def count_construct_RECURSIVE(target, wordbank):
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
            num_ways_rest = count_construct_RECURSIVE(new_target, wordbank)

            total_count += num_ways_rest

    return total_count


def count_construct(target, wordbank, memo):
    if target in dict.keys(memo):
        return memo[target]

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
            num_ways_rest = count_construct(new_target, wordbank, memo)

            total_count += num_ways_rest

    memo[target] = total_count
    return memo[target]


if __name__ == "__main__":
    try:
        # print(can_construct("skateboard", ['skate', "board"], {}))
        # print(
        #     can_construct("enterapotentpot",
        #                   ['a', "p", "ent", "enter", "ot", "o", "t"], {}))

        print(
            count_construct(
                "enterapotentpot",
                ['a', "p", "ent", "enter", "ot", "o", "t"],
                {},
            ))

        print(
            count_construct(
                "purple",
                ['purp', "p", "ur", "le", "purpl"],
                {},
            ))
    except Exception as e:
        print(e)
