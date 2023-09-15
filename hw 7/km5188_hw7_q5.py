from LinkedBinaryTree import LinkedBinaryTree


# a
def create_expression_tree(prefix_exp_str):
    prefix_exp = prefix_exp_str.split(" ")
    operators = "+-/*"
    for index in range(len(prefix_exp)):
        if prefix_exp[index] not in operators:
            prefix_exp[index] = int(prefix_exp[index])
    tuple = create_expression_tree_helper(prefix_exp, 0)
    return LinkedBinaryTree(tuple[0])


def create_expression_tree_helper(prefix_exp, start_pos):
    if isinstance(prefix_exp[start_pos], int):
        node = LinkedBinaryTree.Node(prefix_exp[start_pos])
        return node, 1
    else:
        left = create_expression_tree_helper(prefix_exp, start_pos + 1)
        right = create_expression_tree_helper(prefix_exp, start_pos + 1 + left[1])
        root = LinkedBinaryTree.Node(prefix_exp[start_pos], left[0], right[0])
        return root, left[1] + right[1] + 1


# b
def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    res = ""
    for i in tree.postorder():
        res += str(i.data)+" "
    res = res[:-1]
    return res

