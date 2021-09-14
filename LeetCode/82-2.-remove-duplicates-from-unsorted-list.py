# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list.
#
# Return the linked list sorted as well.

# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]

# Input: head = [1,1,1,2,3]
# Output: [2,3]

from typing import List

# ANCHOR: - Utils


class Node:
    def __init__(self, val, next) -> None:
        self.val = val
        self.next = next


def buildLinkedList(array: List[int]) -> Node:
    prev = n = None

    for val in reversed(array):
        n = Node(val, prev)
        prev = n

    return n


def convertListToArray(head: Node) -> List[int]:
    array = []
    n = head

    while n is not None:
        array.append(n.val)
        n = n.next

    return array


# ANCHOR: - Main


def findNextPossible(start: Node, d: dict) -> Node:
    """
    From the starting point, finds next possible node in linked list that is 
    not a duplicate.
    """
    n = start
    while n is not None and d.get(f"{n.val}") > 1:
        n = n.next
    return n


# We have to traverse the full linked list at least once.
# Time => O(2n) => O(n)
# Space => O(n)
def removeDuplicates(head: Node) -> Node:
    n = head
    d = {}

    # O(n) to get a count of the array
    while n is not None:
        key = f"{n.val}"
        if d.get(key) is None:
            d[key] = 1
        else:
            d[key] += 1
        n = n.next

    # O(n) to go through the array and skip duplicates
    prev = None
    n = head
    while n is not None:
        if d.get(f"{n.val}") > 1:
            # This helper traverses the list and finds the next possible
            # pointer to supplant this one
            next_possible = findNextPossible(n, d)

            if prev is None:
                # If the prev is none, then the duplicates are at the
                # beginning. Replace the "head".
                head = next_possible
            else:
                # "Remove" the duplicates by skipping over them
                prev.next = next_possible

            # Update "n" and keep going
            n = next_possible

        if n is not None:
            prev = n
            n = n.next

    return head


tests = [
    ([1, 3, 7, 4, 6, 3, 7], [1, 4, 6]),
    ([1, 7, 4, 4, 7, 1], []),
    ([], []),
]

try:
    for (input, output) in tests:
        # Build linked list
        head = buildLinkedList(input)

        # Run the algo on the linked list
        r_list = removeDuplicates(head)

        # Convert the LL to an array and compare to the expected output
        r = convertListToArray(r_list)
        print(r)
        assert (r == output)

    print("Success!")

except AssertionError:
    print("Incorrect result")
