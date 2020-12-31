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
            return (float('-inf'), 0, [], [])

        # Finds the max sum on the Left
        left_max_sum, left_path, left_list, left_root_path_list = helper(
            root.left)

        # Finds the max sum on the Right
        right_max_sum, right_path, right_list, right_root_path_list = helper(
            root.right)

        # For debugging:
        # if root.val == tree_root.val:
        #     print('At the root')

        # Calculates the max path using the root.
        # We use max(0, XYZ) because this could be a None value (we are in a leaf!)
        root_max_sum = max(0, left_path) + root.val + max(0, right_path)

        # Compare the 3 max sums and find the largest one
        max_sum = max(left_max_sum, root_max_sum, right_max_sum)

        if left_max_sum == max_sum:
            max_sum_list = left_list
        elif right_max_sum == max_sum:
            max_sum_list = right_list
        else:
            sorted_right = list(reversed(right_root_path_list))
            max_sum_list = left_root_path_list + [root.val] + sorted_right

        # Finds the maximum path including and ending at the root.
        # i.e.: this is the path that is a single line from a leaf node up to the current root node.
        # This can be used "further up the ladder" in order to maybe calculate if the root of this path can join with a different path from the other side and both make up together a better max_sum path.
        root_path = max(left_path, right_path, 0) + root.val

        if (left_path + root.val) == root_path:
            root_path_list = left_list + [root.val]
        elif (right_path + root.val) == root_path:
            root_path_list = right_list + [root.val]
        else:
            root_path_list = [root.val]

        return (max_sum, root_path, max_sum_list, root_path_list)

    result = helper(tree_root)
    # Return the first value of the tuple, which contains the max sum
    return result


if __name__ == '__main__':
    try:
        # ANCHOR: - Test case 1
        max_sum, _, nodes_list, _ = max_root_sum(Node(-1, Node(2), Node(3)))
        print('Follow', nodes_list, 'for a max sum of', max_sum)
        assert max_sum == 4

        # ANCHOR: - Test case 2
        tree_2 = Node(
            -1,
            # Left subtree
            Node(2, Node(4), Node(6)),
            # Rigth subtree
            Node(3, None, Node(7)))
        max_sum, _, nodes_list, _ = max_root_sum(tree_2)
        print('Follow', nodes_list, 'for a max sum of', max_sum)
        assert max_sum == 17

        # ANCHOR: - Test case 3
        tree_3 = Node(
            -3,
            # Left subtree
            Node(4),
            # Rigth subtree
            Node(2, None, Node(5)))
        max_sum, _, nodes_list, _ = max_root_sum(tree_3)
        print('Follow', nodes_list, 'for a max sum of', max_sum)
        assert max_sum == 8

        print('Completed without errors')
    except AssertionError as e:
        print("Assertion error occurred")
