class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(tree_root):
    """
    Traverse the tree and print the values of each node.
    Adaptation of a DFS search.
    """
    start = None
    end = None

    def helper(root):
        if root is None:
            return

        print(root.val)

        helper(root.left)
        helper(root.right)

    helper(tree_root)


def max_root_sum(tree_root):
    def helper(root):
        # If the root is None, we are on a leaf. We cannot add any values from here, so just return.
        if root is None:
            # We return infinite 0 because this is not, and will not be, a possible option
            return (float('-inf'), 0)

        # Finds the max sum on the Left
        left_max_sum, left_path = helper(root.left)

        # Finds the max sum on the Right
        right_max_sum, right_path = helper(root.right)

        if root.val == -1:
            print('At the root')

        # Calculates the max path using the root.
        # We use max(0, XYZ) because this could be a None value (we are in a leaf!)
        root_max_sum = max(0, left_path) + root.val + max(0, right_path)

        # Compare the 3 max sums and find the largest one
        max_sum = max(left_max_sum, root_max_sum, right_max_sum)

        # Finds the maximum path including and ending at the root.
        # i.e.: this is the path that is a single line from a leaf node up to the current root node.
        # This can be used "further up the ladder" in order to maybe calculate if the root of this path can join with a different path from the other side and both make up together a better max_sum path.
        root_path = max(left_path, right_path, 0) + root.val

        return (max_sum, root_path)

    result = helper(tree_root)
    # Return the first value of the tuple, which contains the max sum
    return result[0]


if __name__ == '__main__':
    try:
        tree_2 = Node(
            -1,
            # Left subtree
            Node(2, Node(4), Node(6)),
            # Rigth subtree
            Node(3, None, Node(7)))
        result = max_root_sum(tree_2)
        assert result == 17

        result = max_root_sum(Node(-1, Node(2), Node(3)))
        assert result == 4

        print('Completed without errors')
    except AssertionError as e:
        print("Assertion error occurred")
