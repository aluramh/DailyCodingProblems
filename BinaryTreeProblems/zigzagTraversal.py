from typing import List


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: Node):
    def helper(node: Node):
        if node is None: return

        helper(node.left)
        print(node.val)
        helper(node.right)

    helper(root)


def sorted_array_to_bst(array):
    if len(array) == 0:
        return None

    middle = len(array) // 2
    left = sorted_array_to_bst(array[0:middle])
    right = sorted_array_to_bst(array[(middle + 1):len(array)])

    root = Node(array[middle], left, right)
    return root


def zig_zag_traversal(root: Node):
    buckets = []

    def helper(node: Node, level: int):
        """
        Helper which creates the buckets by traversing levels.
        """
        if node is None:
            return

        if level >= len(buckets):
            # The current level does not exist. Create the new array.
            buckets.append([node.val])
        else:
            # It already exists, so just append it
            buckets[level] += [node.val]

        # Traverse left and right
        helper(node.left, level + 1)
        helper(node.right, level + 1)

    helper(root, False)

    # Traverse the buckets
    for bucket in buckets:
        for val in bucket:
            print(val)

    # Return something
    return True


tests = [
    # [1, 3, 4, 6, 8],
    [1, 2, 3, 4, 5, 6, 7],
]

for t in tests:
    bst = sorted_array_to_bst(t)
    zig_zag_traversal(bst)

print("Finished")
