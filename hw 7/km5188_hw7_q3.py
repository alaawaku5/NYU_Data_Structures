def is_height_balanced(bin_tree):
    def isbal(root):
        if root is None:
            return (0, True)
        else:
            left = isbal(root.left)
            right = isbal(root.right)
            height = max(left[0], right[0]) + 1
            bool_val = left[1] and right[1] and abs(left[0] - right[0]) <= 1

            return (height, bool_val)

    return isbal(bin_tree.root)[1]
