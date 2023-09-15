from BinarySearchTreeMap import BinarySearchTreeMap


def find_min_abs_difference(bst):
    inorder = []
    for i in bst.inorder():
        inorder.append(i.item.key)

    if len(inorder) == 0:
        return
    elif len(inorder) == 1:
        return
    else:
        min_bst = abs(inorder[0] - inorder[1])
        for i in range(1, len(inorder)):
            cur_min = abs(inorder[i] - inorder[i - 1])
            if min_bst > cur_min:
                min_bst = cur_min
    return min_bst

# bst = BinarySearchTreeMap()
# for i in bst.inorder():
