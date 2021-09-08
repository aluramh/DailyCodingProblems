# This problem was asked by Atlassian.

# MegaCorp wants to give bonuses to its employees based on how many lines of
# codes they have written. They would like to give the smallest positive amount
# to each worker consistent with the constraint that if a developer has
# written more lines of code than their neighbor, they should receive more
# money.

# Given an array representing a line of seats of employees at MegaCorp,
# determine how much each one should get paid.

# For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].

# [10, 40, 200, 1000, 60, 30]
# [1, 2, 3, 4, 2, 1]

# [30, 60, 1000, 200, 40, 10]
# [1, 2, 3, , 2, 1]

# zero down to the middle?

# 2 passes?

# recursive?

# If greater than the right, then the bonus will be +1 is whatever on the right


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

        # Else, we want to add a "1", but we could be breaking the rules, so we need to perform some checks...
        else:
            # Check if the current is "1", because we cannot have 2 consecutive "1"s. One has to be larger.
            if payments[i] == 1:
                # If it is "1", then, we need to keep the constant going, so we need to compare
                # and decide where the 2 minimum values go where.
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


try:
    tests = [
        ([10, 40, 200, 1000, 60, 30], [1, 2, 3, 4, 2, 1]),
        ([30, 60, 1000, 200, 40, 50], [1, 2, 3, 2, 1, 2]),
    ]

    for test, expected in tests:
        r = compute_employee_bonuses(test)
        assert (expected == r)

    print("Finished successfully!")

except AssertionError:
    print("Error!")
