class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def _get_root_node(self):
        return Node(self.val, self.left, self.right)

    def pretty_print(self):
        store = {}

        def group_levels(node, level):
            if node is not None:
                if store.get(level) is None:
                    store[level] = [node.val]
                else:
                    store[level] += [node.val]

                group_levels(node.left, level + 1)
                group_levels(node.right, level + 1)

            else:
                if store.get(level) is None:
                    store[level] = ["X"]
                else:
                    store[level] += ["X"]

        group_levels(self._get_root_node(), 0)

        for key, val in store.items():
            print(val)

    def inorder(self):
        arr = []

        def helper(node):
            if node is not None:
                helper(node.left)
                arr.append(node.val)
                helper(node.right)

        helper(Node(self.val, self.left, self.right))
        print(arr)

    def fix(self):
        def helper(node):
            



def sorted_array_to_bst(array):
    if len(array) == 0:
        return None

    middle = len(array) // 2
    left = sorted_array_to_bst(array[0:middle])
    right = sorted_array_to_bst(array[(middle + 1):len(array)])

    root = Node(array[middle], left, right)
    return root

 
tests = [
    # [1, 3, 4, 6, 8],
    [1, 2, 3, 4, 5, 6, 7],
]

for arr in tests:
    bst = sorted_array_to_bst(arr)

    # Mess up BST
    aux = bst.val
    bst.val = bst.left.left.val
    bst.left.left.val = aux

    # Confirm it is messed up
    bst.inorder()

    # Fix it
    bst.fix()

    # Confirm it was fixed
    bst.inorder()
