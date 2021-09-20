from typing import List, Tuple


def max_tower_of_people(people: List[Tuple[int, int]]):
    """
    Main function that sets up the data for the recursion
    """
    # in-place sort by height
    people.sort(key=lambda x: x[0])

    # get a list of only the weights
    height_list = list(map(lambda x: x[1], people))

    result = max_contiguous_sum(height_list)
    return result


def max_contiguous_sum(nums):
    """
    Get the longest sequence for each number and keep track of the longest overall
    
    Time complexity = O(n)
    Space = O(n^2)
    """
    # Iterate through each num, and get the longest road that includes this actual number and store it in memo
    all_sequences = []
    best_sequence = []

    for i in range(len(nums)):
        seq_at_index = best_seq_at_index(nums, all_sequences, i)
        all_sequences.append(seq_at_index)

        # Check if this sequence is better (longer) than the current best
        if len(seq_at_index) > len(best_sequence):
            best_sequence = seq_at_index

    return best_sequence


def best_seq_at_index(nums, sequences, current_index):
    """
    Get the best sequence of a number by iterating through all the best solutions
    previous to the current index, where we can use the current_value.
    Return the longest previous solution where we can add the current value.

    Time complexity = O(n)
    Space = O(n)
    """
    # initialize a best sequence var to track this
    best_sequence = []
    # get the current value
    value = nums[current_index]

    # loop through the array of best sequences at each index, up until the [current_index]
    # (which we're just computing at this point)
    # What we want to do is find the best past sequence where we can append the current value.
    for i in range(current_index):
        # Get the previous best sequence at [i]
        solution = sequences[i]

        # Check if we can append the current num to this seq we are comparing
        # (but don't add it yet)
        if solution[-1] < value:
            # If it's possible to add it AND it's better than the current best,
            # then we update the best sequence at this [current_index]
            if len(solution) > len(best_sequence):
                best_sequence = solution

    # Now that we have the best sequence where we can add the value, add it and return
    return best_sequence + [value]


tests = [
    ([(64, 100), (70, 110), (60, 120), (65, 125)], 2),
    ([(2, 14), (4, 11), (5, 12), (3, 10), (1, 13)], 3),
    ([], 100),
]

try:
    expected = None
    r = []
    for (A, expected) in tests:
        r = max_tower_of_people(A)
        assert len(r) == expected
        print(f"{len(r)} == {expected}? ✅")
        expected = None
        r = []

    print("Success!")
except AssertionError:
    print(f"{len(r)} == {expected}? ❌")
    print("Error!")
