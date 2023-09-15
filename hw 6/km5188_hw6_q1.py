from DoublyLinkedList import DoublyLinkedList


class LinkedQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def enqueue(self, item):
        return self.data.add_last(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.data.delete_first()

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.data.header.next.data



