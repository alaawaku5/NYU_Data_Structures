from DoublyLinkedList import DoublyLinkedList
from LinkedBinaryTree import LinkedBinaryTree
from ArrayStack import ArrayStack

n9 = LinkedBinaryTree.Node(9)
n11 = LinkedBinaryTree.Node(11)
n1 = LinkedBinaryTree.Node(1, n9, n11)

n4 = LinkedBinaryTree.Node(4)
n6 = LinkedBinaryTree.Node(6, n1, n4)

n3 = LinkedBinaryTree.Node(3)
n7 = LinkedBinaryTree.Node(7, n3, n6)

tree = LinkedBinaryTree(n7)


# 1

def bt_even_sum(root):
    if root is None:
        return 0
    else:
        if root.data % 2 == 0:
            return bt_even_sum(root.left) + bt_even_sum(root.right) + root.data
        return bt_even_sum(root.left) + bt_even_sum(root.right)


print(bt_even_sum(n7))


# 2

def bt_contains(root, val):
    if root is None:
        return False
    elif root.data == val:
        return True
    return bt_contains(root.left, val) or bt_contains(root.right, val)


print(bt_contains(n7, 2))


# 3

def is_full(root):
    if root is None:
        return True
    if root.left and root.right:
        return is_full(root.left) and is_full(root.right)
    else:
        return False
    # return (root.left and root.right) and is_full(root.left) and is_full(root.right)


print(is_full(n7))


# midterm 2 question 3,5
def insert_sorted(srt_lnk_lst, elem):
    node_to_insert = DoublyLinkedList.Node(elem)
    if elem < srt_lnk_lst.header.next.data:

        temp = srt_lnk_lst.header.next

        srt_lnk_lst.header.next = node_to_insert
        node_to_insert.prev = srt_lnk_lst.header

        node_to_insert.next = temp
        temp.prev = node_to_insert

    elif elem > srt_lnk_lst.trailer.prev.data:

        temp = srt_lnk_lst.trailer.prev
        srt_lnk_lst.trailer.prev = node_to_insert

        node_to_insert.next = srt_lnk_lst.trailer
        node_to_insert.prev = temp

        temp.next = node_to_insert
    else:
        cursor = srt_lnk_lst.header
        while elem > cursor.next.data:
            cursor = cursor.next
        temp = cursor.next

        cursor.next = node_to_insert
        node_to_insert.prev = cursor

        node_to_insert.next = temp
        temp.prev = node_to_insert


dll = DoublyLinkedList()
dll.add_last(2)
dll.add_last(3)
dll.add_last(5)
dll.add_last(7)
dll.add_last(12)
print(dll)

# q3
insert_sorted(dll, 0)
print(dll)


# q5
class DubStack:
    def __init__(self):
        self.data = ArrayStack()
        self.n = 0

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return self.n

    def push(self, elem):
        self.n += 1
        if len(self) > 0 and self.top() == elem:
            topped = self.data.top()
            top_occ = topped[1] + 1
            self.data.pop()
            self.data.push((elem, top_occ))
        else:
            self.data.push((elem, 1))

    def top(self):
        if self.data.is_empty():
            raise Exception
        return self.data.top()[0]

    def top_dups_count(self):
        if self.data.is_empty():
            raise Exception
        return self.data.top()[1]

    def pop(self):
        self.n -= 1
        if self.data.is_empty():
            raise Exception

        if self.data.top()[1] == 1:
            popped = self.data.pop()
            return popped[0]
        else:
            popped = self.data.pop()
            top_occ = popped[1] - 1
            e = popped[0]
            self.data.push((e, top_occ))
            return e

    def pop_dups(self):

        if len(self) == 0:
            raise Exception
        popped = self.data.pop()
        self.n -= popped[1]
        return popped[0]

#
# dstack = DubStack()
# dstack.push(4)
# dstack.push(4)
# dstack.push(4)
# print(dstack.__len__())
#
# # print(dstack.top())
# print(dstack.__len__())
# print(dstack.pop)
# print(dstack.__len__())



# 4 preorder with stack
from ArrayQueue import ArrayQueue


class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def count_nodes(self):
        def subtree_count(root):
            if (root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return 1 + left_count + right_count

        return subtree_count(self.root)

    def sum(self):
        def subtree_sum(root):
            if (root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return root.data + left_sum + right_sum

        return subtree_sum(self.root)

    def height(self):
        def subtree_height(root):
            if (root.left is None and root.right is None):
                return 0
            elif (root.left is None):
                return 1 + subtree_height(root.right)
            elif (root.right is None):
                return 1 + subtree_height(root.left)
            else:
                left_height = subtree_height(root.left)
                right_height = subtree_height(root.right)
                return 1 + max(left_height, right_height)

        if (self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)

    def preorder(self):
        def subtree_preorder(root):
            if (root is None):
                pass
            else:
                yield root
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)

    def preorder_with_stack(self):
        s = ArrayStack()
        root = self.root
        tree_str = ""
        s.push(root)
        while not s.is_empty():
            last = s.pop()
            yield last.data
            if last.right:
                s.push(last.right)
            if last.left:
                s.push(last.left)

    def postorder(self):
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)

    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)

    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data
