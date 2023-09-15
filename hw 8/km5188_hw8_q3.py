from BinarySearchTreeMap import BinarySearchTreeMap


def restore_bst(prefix_lst):
    def helper(prefix_lst):
        n = len(prefix_lst)
        if n == 0:
            return None

        root_item = BinarySearchTreeMap.Item(prefix_lst[0])
        root = BinarySearchTreeMap.Node(root_item)
        stack = []
        stack.append(root)
        for i in range(1, n):
            parent = stack[-1]
            curr = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[i]))
            while (len(stack)!= 0) and stack[-1].item.key < curr.item.key:
                parent = stack.pop()
            if parent.item.key > curr.item.key:
                parent.left = curr
                curr.parent = parent
            else:
                parent.right = curr
                curr.parent = parent
            stack.append(curr)
        return root

    root = helper(prefix_lst)
    tree = BinarySearchTreeMap()
    tree.root = root
    return tree

