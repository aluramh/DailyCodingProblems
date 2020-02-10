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


SEPARATOR = '_'


def traverse(node, index, array):
    # Append first the parent child
    parsed_val = node.val if node is not None else 'X'
    array.append((index, parsed_val))
    print(parsed_val)

    # Then traverse the left
    if node is not None:
        traverse(node.left, index * 2, array)
        traverse(node.right, (index * 2) + 1, array)


def sort_tuples(tuples):
    # Sort the tuples
    tuples.sort(key=lambda x: x[0])

    # "Flatten" the tuples in the array
    result = []
    for tuple_item in tuples:
        result.append(tuple_item[1])

    # Return array representation of BST
    return result


def serialize(root):
    # Traverse Nodes and generate a BST array (unsorted)
    array = []
    traverse(root, 1, array)

    # Sort the array
    array_bst = sort_tuples(array)
    print({'array_bst': array_bst}, '\n')

    return SEPARATOR.join(array_bst)


def deserialize(s):
    print(s)

    # Split from string using separator
    separated = s.split(SEPARATOR)

    # Remove last item since, invariantly, will always be empty string
    del separated[len(separated) - 1]

    # print(separated)

    # Loop through items and rebuild BST nodes
    def build(index, array):
        i = index - 1

        # e.g.: [1]
        if i == (len(array) - 1):
            return Node(array[i - 1], None, None)

        else:
            left = build(i * 2, array)
            right = build((i * 2) + 1, array)
            return Node(array[i - 1], left, right)

    return build(1, [2])


def rebuild(root, i, array):
    if i >= len(array):
        return

    left = rebuild(array[i * 2], i, array)
    right = rebuild(array[(i * 2) + 1], i, array)
    return Node(array[i], left, right)


# node = Node(
#     'root',
#     Node(
#         'left',
#         Node('left.left')
#     ),
#     Node('right')
# )

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# serialized_node = serialize(node)
# serial_deserial = deserialize(serialized_node)


def main():
    def build(index, array):
        i = index - 1

        # e.g.: [1]
        if i == (len(array) - 1):
            return Node(array[i - 1], None, None)

        else:
            left = build(i * 2, array)
            right = build((i * 2) + 1, array)
            return Node(array[i - 1], left, right)

    return build(1, [2])


r = main()
traverse(r[0], 0, r)
print(main())