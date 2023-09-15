from BinarySearchTreeMap import BinarySearchTreeMap

def create_chain_bst(n):
    bst = BinarySearchTreeMap()
    for num in range(1, n + 1):
        bst[num] = None
    return bst


def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst


def add_items(bst, low, high):
    if low == high:
        new_item = BinarySearchTreeMap.Item(low)
        new_node = BinarySearchTreeMap.Node(new_item)
    else:
        mid = (low + high) // 2
        new_item = BinarySearchTreeMap.Item(mid)
        new_node = BinarySearchTreeMap.Node(new_item)

        right = add_items(bst, mid + 1, high)
        left = add_items(bst, low, mid - 1)

        new_node.left = left
        left.parent = new_node
        new_node.right = right
        right.parent = new_node

    if bst.is_empty():
        bst.root = new_node

    return new_node

#
# tree = create_complete_bst(3)
# for i in tree:
#     print(i)
#
# bst = BinarySearchTreeMap()