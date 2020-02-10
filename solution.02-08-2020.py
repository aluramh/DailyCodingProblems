# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes
# the tree into a string, and deserialize(s), which deserializes the string back
# into the tree.

# For example, given the following Node class
# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Constants
ROOT = Node('root', Node('left', Node('left.left')), Node('right'))
SEPARATOR = '  '


def serialize(node, show=False):
    nodes = []

    def helper(node, i):
        if node:
            nodes.append((i, node.val))

        elif node is None:
            nodes.append((i, 'X'))

        if node is not None:
            helper(node.left, i * 2)
            helper(node.right, i * 2 + 1)

    # Generate
    helper(node, 1)

    # Sort
    nodes.sort(key=lambda x: x[0])

    # Remove index and leave just val
    final = map(lambda x: x[1], nodes)

    # Generate string
    s = SEPARATOR.join(list(final))

    if show:
        print(s)

    return


serialize(ROOT, True)
