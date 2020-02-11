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


# O(2n)
def serialize(node):
    nodes = []

    def helper(node):
        if node:
            nodes.append(node.val)

        elif node is None:
            nodes.append(EMPTY)

        if node is not None:
            helper(node.left)
            helper(node.right)

    # O(n)
    helper(node)

    # O(n) for joining string
    return SEPARATOR.join(nodes)


# O(n)
def lisp_serialize(node):
    if node is None:
        return EMPTY

    right = lisp_serialize(node.right)
    left = lisp_serialize(node.left)
    return '({} ({} {}))'.format(node.val, left, right)


# O(n)
def deserialize(s):
    # Returns a node with all the left/right
    def helper():
        val = next(vals)
        # print('NEXT VALS ==>', val)

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
s = serialize(ROOT)
print(s)

# Serialize similar to lisp
lisp = lisp_serialize(ROOT)
print(lisp)

# Deserialize
d = deserialize(s)
print(serialize(d))

try:
    assert deserialize(serialize(ROOT)).left.left.val == 'left.left'
    print("Test passed!")
except AssertionError as error:
    print("Test failed :(")
