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


def removeDuplicates(head: Node) -> Node:
    prev = None
    n = head

    # Traverse through the whole list once
    while n is not None:
        nxt = n.next

        if nxt is not None and n.val == nxt.val:
            # Are these duplicated?
            while n.val == nxt.val:
                n = nxt.next

            # Once we exit the loop, then the next possible val is "n"
            prev.next = n

        # Always move forward in the list
        prev = n
        n = n.next

    return head


tests = [
    ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
    ([1, 1, 1, 2, 3], [2, 3]),
]

try:
    for (input, output) in tests:
        # Build linked list
        head = buildLinkedList(input)

        # Run the algo on the linked list
        r_list = removeDuplicates(head)

        # Convert the LL to an array and compare to the expected output
        r = convertListToArray(r_list)
        assert (r == output)

except AssertionError:
    print("Error")
