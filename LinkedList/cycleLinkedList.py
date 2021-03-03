class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def createLL() -> Node:
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)

    # Add the cycles
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six
    six.next = two

    return one


def createLL2() -> Node:
    zero = Node(0)
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)

    # Add the cycles
    zero.next = one
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    five.next = six
    six.next = seven
    seven.next = two

    return zero


def isThereACycle(head) -> bool:
    if head is None: return False

    slow = fast = head

    while slow and (fast and fast.next):
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def findFirstCycle(head):
    """
    Input:
        - Head of a linked list that has a cycle
    Output:
        - Node where the cycle first starts
    """

    slow = fast = head

    while slow and (fast and fast.next):
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Reset slow to the beginning
            slow = head

            # Move at the same speed until they find each other
            while slow != fast:
                fast = fast.next
                slow = slow.next

            return slow

    return False


if __name__ == "__main__":
    tests = [
        # (createLL(), True, 2),
        # (createLL().next.next.next, True, createLL().next.next.next.val),
        (createLL2(), True, 2),
        # (None, False, None),
    ]

    for (linked_list, expected_result, cycle_start_node) in tests:
        result = isThereACycle(linked_list)
        print('Cycle?', result)

        if result is True:
            first_cycle_node = findFirstCycle(linked_list)
            print("Cycle starts at:", first_cycle_node.val)
            assert first_cycle_node.val == cycle_start_node

        print()
