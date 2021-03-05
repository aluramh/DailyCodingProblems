import sys
sys.setrecursionlimit(15000)


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(queries) -> Node:
    # Initialize the root of the tree
    root = Node(1)
    # Initialize queue with items
    queue = [root]
    # queue = [Node(2)] + queue
    # queue = [Node(3)] + queue

    # NOTE: - There is the exact amount of queries to sync with the queue
    for (left_val, right_val) in queries:
        current_node = queue.pop()

        if left_val != -1:
            # Create the nodes
            left_node = Node(left_val)
            # Attach them to the current root
            current_node.left = left_node
            # And add them to the queue of items that need to be handled
            queue = [left_node] + queue

        if right_val != -1:
            right_node = Node(right_val)
            current_node.right = right_node
            queue = [right_node] + queue

    # Return the root, which will now contain the tree
    return root


# def swapNodesRecursive(indexes, queries):
#     def inorder_traversal(root: Node) -> str:
#         stack = []

#         current_node = root
#         while len(stack) > 0 or current_node:
#             # Push all the items to the left until we find one that is null
#             while current_node:
#                 stack = stack + [current_node]
#                 current_node = current_node.left

#             # Now we can check the stack
#             if len(stack) > 0:
#                 popped_item = stack.pop()
#                 print(popped_item.val)
#                 current_node = popped_item.right
#             else:
#                 # we are done here
#                 pass

#     def swapNodesAtDepthMultiplesK(root: Node, k: int):
#         """
#         Multiples of K
#         """
#         def helper(node, depth):
#             if node is None: return

#             # Traverse the nodes
#             helper(node.left, depth + 1)
#             helper(node.right, depth + 1)

#             # Swap the nodes if the depth is a multiple
#             if depth % k == 0:
#                 aux_node = node.right
#                 node.right = node.left
#                 node.left = aux_node

#         helper(root, 1)

#     # Build the tree
#     root = buildTree(indexes)

#     # Loop through, and execute, the queries
#     results = []
#     for query in queries:
#         # Swap the nodes according to the query
#         swapNodesAtDepthMultiplesK(root, query)
#         # Print the inorder tree
#         result = inorder_traversal(root)
#         results.append(result)
#         print(result)

#     return results


def swapNodesIterative(indexes, queries):
    def inorder_traversal(root: Node) -> str:
        current_node = root
        stack = []
        result = []

        while len(stack) > 0 or current_node:
            # Push current node to stack for later use
            while current_node:
                stack = stack + [current_node]
                current_node = current_node.left

            # The left item is none. So we pop the item at the top of the stack
            popped_item = stack.pop()
            # "read" the current item
            result.append(str(popped_item.val))
            # Traverse to the right and repear
            current_node = popped_item.right

        return " ".join(result)

    def swapNodesAtDepthMultiplesK(root: Node, k: int):
        """
        Multiples of K
        """
        stack = []
        current_node = root
        current_depth = 1

        while len(stack) > 0 or current_node:
            # Traverse all the way to the left
            while current_node:
                stack.append((current_node, current_depth))
                current_node = current_node.left
                current_depth += 1

            # No more items? pop from the stack
            popped_node, popped_depth = stack.pop()
            # print(popped_node.val, depth)

            # Update the current vals
            current_node = popped_node.right
            current_depth = popped_depth + 1

            # Since we have popped this, then it's not going to be used in the
            # future, so we can swap l/r
            if popped_depth % k == 0:
                aux = popped_node.right
                popped_node.right = popped_node.left
                popped_node.left = aux

    # Build the tree
    root = buildTree(indexes)

    # Loop through, and execute, the queries
    results = []
    for query in queries:
        # Swap the nodes according to the query
        swapNodesAtDepthMultiplesK(root, query)
        # Print the inorder tree
        result = inorder_traversal(root)
        results.append(result)
        print(result)

    return results


# ANCHOR: - Main

tests = [
    (
        [[2, 3], [-1, -1], [-1, -1]],
        [1, 1],
        ["3 1 2", "2 1 3"],
    ),
    (
        [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1],
         [10, 11], [-1, -1], [-1, -1], [-1, -1]],
        [2, 4],
        ["2 9 6 4 1 3 7 5 11 8 10", "2 6 9 4 1 3 7 5 10 8 11"],
    ),
    (
        [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13],
         [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1],
         [-1, -1], [-1, -1], [-1, -1]],
        [2, 3],
        [
            "14 8 5 9 2 4 13 7 12 1 3 10 15 6 17 11 16",
            "9 5 14 8 2 13 7 12 4 1 3 17 11 16 6 10 15"
        ],
    ),
]

for (indexes, queries, expected_results) in tests:
    result = swapNodesIterative(indexes, queries)
    assert result == expected_results

print("Success!")
