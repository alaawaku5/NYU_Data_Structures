# 1
class DoublyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None

    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val):
        new_node = DoublyLinkedList.Node(val)
        prev_node = node
        next_node = node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        self.n += 1
        return new_node

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_after(self.trailer.prev, val)

    def add_before(self, node, val):
        return self.add_after(node.prev, val)

    def delete_node(self, node):
        data = node.data
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.n -= 1
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.trailer.prev)

    def __iter__(self):
        cursor = self.header.next
        while (cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return '[' + " <--> ".join([str(elem) for elem in self]) + ']'

    def remove_all(self, elem):
        cursor = self.header.next
        while (cursor.next is not None):
            if (cursor.data == elem):
                next_node = cursor.next
                self.delete_node(cursor)
                cursor = next_node
            else:
                cursor = cursor.next

    def mid_push(self, e):
        m = len(n) // 2 + 1
        cursor = self.header.next
        for i in range(m):
            cursor = cursor.next
        self.data.add_before(cursor)

    def __getitem__(self, item):
        if item < 0 or item > self.n:
            raise IndexError

        elif item <= self.n // 2:
            cursor = self.header.next
            for i in range(item):
                cursor = cursor.next

        elif item > self.n // 2:
            cursor = self.trailer.prev
            if item == len(self):
                raise IndexError()
            for i in range(len(self) - item - 1):
                cursor = cursor.prev

        return cursor.data


class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.add_last(e)

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data.header.next()

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        popped = self.data.trailer.prev
        self.data.delete_node(popped)
        return popped


# 2

class DoublyLinkedList_Get:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None

    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val):
        new_node = DoublyLinkedList.Node(val)
        prev_node = node
        next_node = node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node
        self.n += 1
        return new_node

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_after(self.trailer.prev, val)

    def add_before(self, node, val):
        return self.add_after(node.prev, val)

    def delete_node(self, node):
        data = node.data
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.n -= 1
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        return self.delete_node(self.trailer.prev)

    def __iter__(self):
        cursor = self.header.next
        while (cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return '[' + " <--> ".join([str(elem) for elem in self]) + ']'

    def remove_all(self, elem):
        cursor = self.header.next
        while (cursor.next is not None):
            if (cursor.data == elem):
                next_node = cursor.next
                self.delete_node(cursor)
                cursor = next_node
            else:
                cursor = cursor.next

    def __getitem__(self, item):
        if item < 0 or item > self.n:
            raise IndexError

        elif item <= self.n // 2:
            cursor = self.header.next
            for i in range(item):
                cursor = cursor.next

        elif item > self.n // 2:
            cursor = self.trailer.prev
            if item == len(self):
                raise IndexError()
            for i in range(len(self) - item - 1):
                cursor = cursor.prev

        return cursor.data


dll = DoublyLinkedList_Get()
dll.add_last(1)
dll.add_last(2)
dll.add_last(3)
dll.add_last(4)
dll.add_last(5)


# print(dll)
# print(dll[4])


# 3
class dll_MidStack():
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.add_last(e)

    def top(self, e):
        return self.data[0]

    def pop(self):
        return self.data.delete_last()

    def mid_push(self, e):
        m = len(n) // 2 + 1
        cursor = self.header.next
        for i in range(m):
            cursor = cursor.next
        self.data.add_before(cursor)


# 4
d = DoublyLinkedList()
d.add_last(1)
d.add_last(2)
d.add_last(3)
d.add_last(4)
d.add_last(5)


# d.add_last(6)


def reverse_dll_by_data(dll):
    if len(dll) % 2 == 0:
        mid = len(dll) // 2
    else:
        mid = len(dll) // 2 - 1

    s = dll.header.next
    e = dll.trailer.prev

    for i in range(mid - 1):
        s.data, e.data = e.data, s.data
        s = s.next
        e = e.next

    return dll


print(reverse_dll_by_data(d))


# 4b
def reverse_dll_by_node(dll):
    if len(dll) % 2 == 0:
        mid = len(dll) // 2
    else:
        mid = len(dll) // 2 - 1

    for i in range(mid - 1):
        s = dll.header.next
        s = s.next

        e = dll.trailer.prev
        e = e.next

        s, e = e, s

    return dll


print(reverse_dll_by_node(d))


# 5
class SinglyLinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

        def disconnect(self):
            self.data = None
            self.next = None

    def __init__(self):
        self.header = SinglyLinkedList.Node()
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size

    def add_after(self, node, val):
        new_node = SinglyLinkedList(val)
        prev_node = node
        next_node = node.next
        prev_node.next = new_node
        new_node.next = next_node
        self.size += 1
        return new_node

    def add_before(self, node, val):
        cursor = self.header.next
        while cursor.next is not node:
            cursor = cursor.next

        self.add_after(cursor)

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        cursor = self.header.next
        while cursor.next is not None:
            cursor = cursor.next

        self.add_after(cursor)

    def delete_node(self, node):
        prev = self.header.next
        while prev.next is not node:
            prev = prev.next

        data = node.data
        next_node = node.next
        prev.next = next_node

        self.size -= 1
        node.disconnect()
        return data

    def delete_first(self):
        return self.delete_node(self.header.next)

    def delete_last(self):
        last = self.header.next
        while last.next is not None:
            last = last.next
        return self.delete_node(last)

    def __iter__(self):
        cursor = self.header.next
        while cursor is not None:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return '[' + " -> ".join([str(elem) for elem in self]) + ']'
