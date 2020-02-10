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


def deserialize(s):
    print(s)


def traverse(node, index, array):
    # Append first the parent child
    parsed_val = node.val if node is not None else None
    array.append((index, parsed_val))

    # Then traverse the left
    if node is not None:
        traverse(node.left, index * 2, array)
        traverse(node.right, (index * 2) + 1, array)


def sort(tuples):
    print(tuples)


def serialize(root):
    array = []
    traverse(root, 1, array)
    print(1, array)


# node = Node(
#     'root',
#     Node(
#         'left',
#         Node('left.left')
#     ),
#     Node('right')
# )

node = Node('root', Node('left', Node('left.left')), Node('right'))
serialized_node = serialize(node)
