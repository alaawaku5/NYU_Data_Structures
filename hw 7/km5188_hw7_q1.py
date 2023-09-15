from LinkedBinaryTree import LinkedBinaryTree
from ArrayQueue import ArrayQueue

def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        if root.left is None and root.right is None:
            return root.data, root.data
        elif root.left is None:
            return min(subtree_min_and_max(root.right)[0], root.data), max(subtree_min_and_max(root.right)[1], root.data)
        elif root.right is None:
            return min(subtree_min_and_max(root.left)[0], root.data), max(subtree_min_and_max(root.left)[1], root.data)
        else:
            return min(subtree_min_and_max(root.left)[0], subtree_min_and_max(root.right)[0], root.data), max(subtree_min_and_max(root.left)[1], subtree_min_and_max(root.right)[1], root.data)

    if bin_tree.root is None:
        raise Exception('Tree is empty')
    else:
        return subtree_min_and_max(bin_tree.root)


