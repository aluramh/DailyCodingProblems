def can_construct_RECURSIVE(target, wordbank):
    if target == '':
        return True

    for word in wordbank:
        is_prefix = target.find(word) == 0

        if is_prefix:
            # Remove the prefix from the string to create a new target
            new_target = target[target.index(word) + len(word):len(target)]
            if (can_construct_RECURSIVE(new_target, wordbank) is True):
                return True

    return False


def can_construct(target, wordbank, memo):
    if target in dict.keys(memo):
        return memo[target]

    if target == '':
        return True

    for word in wordbank:
        is_prefix = target.find(word) == 0

        if is_prefix:
            # Remove the prefix from the string to create a new target
            new_target = target[target.index(word) + len(word):len(target)]

            # Computed value
            is_constructible = can_construct(new_target, wordbank, memo)
            memo[target] = is_constructible

            if (is_constructible is True):
                return is_constructible

    memo[target] = False
    return False


if __name__ == "__main__":
    try:
        # print(can_construct("skateboard", ['skate', "board"], {}))
        # print(
        #     can_construct("enterapotentpot",
        #                   ['a', "p", "ent", "enter", "ot", "o", "t"], {}))
        print(
            can_construct("eeeeeeeeeeeeeeeeeeeeeeeef", [
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