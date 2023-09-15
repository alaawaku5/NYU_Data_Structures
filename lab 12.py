# q1
from BinarySearchTreeMap import BinarySearchTreeMap


def min_max_BST(bst):
    min_cursor = bst.root
    while min_cursor.left is not None:
        min_cursor = min_cursor.left

    max_cursor = bst.root
    while max_cursor.right is not None:
        max_cursor = max_cursor.right

    return min_cursor.item.key, max_cursor.item.key


root_node = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(5))
bst = BinarySearchTreeMap()
bst.root = root_node

bst.insert(2, None)
bst.insert(1, None)
bst.insert(3, None)

bst.insert(12, None)
bst.insert(9, None)
bst.insert(21, None)
bst.insert(19, None)
bst.insert(25, None)

print(min_max_BST(bst))


# 2
def glt_n(bst, n):
    cursor = bst.root
    glt = None
    while cursor is not None:

        if cursor.item.key == n:
            return cursor.item.key
        elif cursor.item.key > n:
            if cursor.left is not None and cursor.left.item.key < n:
                glt = cursor.left.item.key
            cursor = cursor.left

        elif cursor.item.key < n:
            if cursor.right is not None and cursor.right.item.key >= n:
                glt = cursor.item.key
            cursor = cursor.right

    return glt


print(glt_n(bst, 20))


def compare_BST(bst1, bst2):
    lst1 = []
    for key in bst1:
        lst1.append(key)

    lst2 = []
    for key in bst2:
        lst2.append(key)

    print(lst1, lst2)
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False

    return True


root_node = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(15))
bst1 = BinarySearchTreeMap()
bst1.root = root_node

bst1.insert(10, None)
bst1.insert(20, None)
bst1.insert(5, None)
bst1.insert(12, None)

root2 = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(15))
bst2 = BinarySearchTreeMap()
bst2.root = root2

bst2.insert(12, None)
bst2.insert(20, None)
bst2.insert(5, None)
bst2.insert(10, None)

print(compare_BST(bst1, bst2))


def is_BST(root):
    return is_BST_helper(root)


def is_BST_helper(root):
    if root.left is None and root.right is None:
        return (root.data, root.data), True

    elif root.left and root.right:
        left = is_BST_helper(root.left)  # ((2,5), True)
        right = is_BST_helper(root.right)
        bool_val = (root.data >= left[0][1]) and (root.data <= right[0][0]) and left[1] and right[1]

        return (left[0][0], right[0][1]), bool_val

    elif root.left:
        left = is_BST_helper(root.left)  # ((2,5), True)
        bool_val = (root.data >= left[0][1]) and left[1]
        return (left[0][0], root.data), bool_val

    elif root.right:
        right = is_BST_helper(root.right)
        bool_val = (root.data <= right[0][0]) and right[1]
        return (root.data, right[0][1]), bool_val
