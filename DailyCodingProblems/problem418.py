# This problem was asked by Atlassian.

# MegaCorp wants to give bonuses to its employees based on how many lines of
# codes they have written. They would like to give the smallest positive amount
# to each worker consistent with the constraint that if a developer has
# written more lines of code than their neighbor, they should receive more
# money.

# Given an array representing a line of seats of employees at MegaCorp,
# determine how much each one should get paid.

# For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].


def compute_employee_bonuses(lines):
    if len(lines) == 0:
        return []
    if len(lines) == 1:
        return [1]

    # Initilize new array with min payment possible
    payments = [0] * len(lines)

    # initialize minimum pay
    payments[0] = 1

    i = 0
    while i < len(lines) - 1:
        # If greater, then keep increasing
        if lines[i] < lines[i + 1]:
            payments[i + 1] = payments[i] + 1

        # Else, we want to add a "1", but we could be breaking the rules, so
        # we need to perform some checks...
        else:
            # Check if the current is "1", because we cannot have 2
            # consecutive "1"s. One has to be larger.
            if payments[i] == 1:
                # If it is "1", then, we need to keep the constant going, so
                # we need to compare and decide where the 2 minimum values go
                # where.
                if lines[i] < lines[i + 1]:
                    payments[i] = 1
                    payments[i + 1] = 2
                else:
                    payments[i] = 2
                    payments[i + 1] = 1

            # If adding a "1" does not impact the rules, then add it
            else:
                payments[i + 1] = 1

        i += 1

    return payments


def compute_employee_bonuses2(lines):
    payments = [1] * len(lines)

    # Make sure that all the items are always at least +1 greater than the
    # items on their left.
    for i in range(1, len(lines)):
        if lines[i] > lines[i - 1]:
            payments[i] = payments[i - 1] + 1

    # Make a 2nd pass and make sure that all the items fulfill the rule the
    # other way around.
    # In this case, we want the current item to the max() of either its
    # current value, or +1 than the item on its right.
    i = len(lines) - 2
    while i >= 0:
        if lines[i] > lines[i + 1]:
            payments[i] = max(payments[i], payments[i + 1] + 1)
        i -= 1

    return payments


try:
    tests = [
        ([10, 40, 200, 1000, 60, 30], [1, 2, 3, 4, 2, 1]),
        ([30, 60, 1000, 200, 40, 50], [1, 2, 3, 2, 1, 2]),
        ([30, 60, 80], [1, 2, 3]),
        ([80, 60, 80], [2, 1, 2]),
        ([80, 50], [2, 1]),
        (
            [
                10, 40, 200, 1000, 60, 30, 200, 1000, 60, 30, 200, 1000, 60,
                30, 200, 1000, 60, 30
            ],
            [1, 2, 3, 4, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1],
        ),
    ]

    for test, expected in tests:
        r = compute_employee_bonuses(test)
        r2 = compute_employee_bonuses2(test)
        assert (r2 == r)
        # assert (expected == r)

    print("Finished successfully!")

except AssertionError:
    print("Error!")
