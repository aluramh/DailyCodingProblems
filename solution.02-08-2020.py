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
EMPTY = 'X'


def serialize(node, show=False):
    nodes = []

    def helper(node):
        if node:
            nodes.append(node.val)

        elif node is None:
            nodes.append(EMPTY)

        if node is not None:
            helper(node.left)
            helper(node.right)

    helper(node)
    return SEPARATOR.join(nodes)


def deserialize(s):
    # Returns a node with all the left/right
    def helper():
        val = next(vals)
        print('NEXT VALS ==>', val)

        # If we reach the end, then it's a leaf and it's the last one
        if val is None or val is 'X':
            return None

        # Returns, recursivelly, the complete Node tree
        node = Node(val, helper(), helper())
        return node

    # Get an iteration from the list of the split data
    vals = iter(s.split(SEPARATOR))

    # Start the helper that returns a node with all the
    # deserialized nodes
    return helper()


# Serialize
l = serialize(ROOT)
print(l)

# Deserialize
d = deserialize(l)
print(serialize(d))
