# linked list class
# single linked list
# doubly linked list

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
        return len(self.n) == 0

    def add_after(self, node, val):
        prev_node = node
        next_node = node.next
        new_node = DoublyLinkedList.node(val)

        new_node.prev = prev_node
        prev_node.next = new_node

        next_node.prev = new_node
        new_node.next = next_node
        self.n += 1
        return new_node

    def add_first(self):
        return self.add_after(self.header, val)

    def add_last(self):
        return self.add_after(self.trailer.prev, val)

    def delete_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.n -= 1
        res = node.data
        node.disconnect()
        return res

    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.delete_node(self.trailor.prev)

    def __iter__(self):
        cursor = head.next
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + "<->".join([str(elem) for elem in self]) + "]"

    def remove_all(self, elem):
        cursor = head.next
        while cursor is not self.trailer:
            if cursor.data == elem:
                next_node = cursor.next
                self.delete_node(cursor)
                cursor = next_node
            else:
                cursor = cursor.next


# is compares references, == compares value
dll = DoublyLinkedList()
dll.add_first('a')
dll.add_first('b')
dll.add_last('c')

# nov 10
