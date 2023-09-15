import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class StaticArrayQueue:
    def __init__(self, max_cap):
        self.data_arr = make_array(max_cap)
        self.capacity = max_cap
        self.n = 0
        self.front_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def is_full(self):
        return (self.n == self.capacity)

    def enqueue(self, item):
        if (self.is_full()):
            raise Exception("Queue is full")
        elif (self.is_empty()):
            self.data_arr[0] = item
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = item
            self.n += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        if (self.is_empty()):
            self.front_ind = None
        return value

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]


class ArrayQueue:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.capacity = ArrayQueue.INITIAL_CAPACITY
        self.n = 0
        self.front_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        if (self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = elem
            self.n += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        if (self.is_empty()):
            self.front_ind = None
        if ((self.n < self.capacity // 4) and
                (self.capacity > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = self.data_arr[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data_arr = new_data
        self.capacity = new_cap
        self.front_ind = 0


class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
        self.summ = 0

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return self.data.is_empty()

    def enqueue(self, e):
        ''' Add element e to the front of the queue.
        If e is not an int or float, raise a TypeError '''
        if type(e) != int and type(e) != float:
            raise TypeError
        else:
            self.data.enqueue(e)
            self.summ += e

    def dequeue(self):
        ''' Remove and return the first element from the queue.
        If the queue is empty, raise an exception'''
        val = self.data.dequeue()
        self.summ -= val
        return val

    def first(self):
        ''' Return a reference to the first element of the queue without removing it.
        If the queue is empty, raise an exception '''
        self.data.first()

    def sum(self):
        ''' Returns the sum of all values in the queue'''
        return self.summ

    def mean(self):
        ''' Return the mean (average) value in the queue'''
        if len(self) == 0:
            avr = 0
        else:
            avr = self.summ / len(self)
        return avr


aaa = MeanQueue()
aaa.enqueue(1)
aaa.enqueue(2)
print(len(aaa))
# print(aaa)
print(aaa.summ)
print(aaa.mean)


# q2
def flatten_list_by_depth(lst):
    q = ArrayQueue()
    new_lst = []

    for elem in lst:
        q.enqueue(elem)

    while not q.is_empty():
        length = len(q)

        for i in range(length)
            front = q.dequeue()

            if isinstance(front, list):
                for elem in front:
                    q.enqueue(elem)

            elif isinstance(last, int):
                new_lst.append(front)

    return new_lst


lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
new_lst = flatten_list_by_depth()
/Users/alaawaku/Desktop/data structures/hw5/hw5 - ArrayDeque.py

# q3
class ArrayDeque:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.capacity = ArrayQueue.INITIAL_CAPACITY
        self.n = 0
        self.front_ind = None
        self.back_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data_arr[self.back_ind]

    def enqueque_first(self, elem):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)

        if (self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.back_ind = 1
            self.n += 1
        else:
            self.front_ind = (self.front_ind - 1) % self.capacity
            self.data_arr[self.front_ind] = elem
            self.n += 1
            # update the back element

    def enqueque_last(self, elem):

        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        if (self.is_empty()):
            self.data_arr[0] = elem
            self.front_ind = 0
            self.n += 1
        else:
            back_ind = (self.front_ind + self.n) % self.capacity
            self.data_arr[back_ind] = elem
            self.n += 1

    def dequeque_first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % self.capacity
        self.n -= 1
        if (self.is_empty()):
            self.front_ind = None
        if ((self.n < self.capacity // 4) and
                (self.capacity > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value

    def dequeque_last(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.back_ind]
        self.data_arr[self.back_ind] = None
        self.back_ind = (self.back_ind - 1) % self.capacity
        self.n -= 1
        if (self.is_empty()):
            self.back_ind = None
        if ((self.n < self.capacity // 4) and
                (self.capacity > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(self.capacity // 2)
        return value

    def resize(self, new_cap):
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = self.data_arr[old_ind]
            old_ind = (old_ind + 1) % self.capacity
        self.data_arr = new_data
        self.capacity = new_cap
        self.front_ind = 0
        self.back_ind = self.front_ind + self.n -1



aq = ArrayDeque()
aq.enqueque_first(1)
aq.enqueque_last(2)
print(aq.last())

# q4
class QueueStack:
    def __init__(self):
        self.data = ArrayQueue()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        pass

    def pop(self):
        pass

    def top(self):
        pass


# lab 10

# q1
# easy
# q2
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
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val):
        new_node = DoublyLinkedList.Node(val)
        prev_node = node
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        next_node.prev = new_node
        new_node.next = next_node
        self.size += 1
        return new_node

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_after(self.trailer.prev, val)

    def add_before(self, node, val):
        return self.add_after(node.prev, val)

    def delete_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if self.is_empty() == True:
            raise Exception("List is empty")
        return self.delete_node(self.header.next)

    def delete_last(self):
        if self.is_empty() == True:
            raise Exception("List is empty")
        return self.delete_node(self.trailer.prev)

    def __iter__(self):
        cursor = self.header.next
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(elem) for elem in self]) + "]"

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
        mid = len(self)//2
        if item <= mid:
            cursor = self.header.next
            for i in range(item):
                cursor = cursor.next

        elif item>mid:
            cursor = self.trailer.prev
            for i in range(len(self)-item-1):
                cursor = cursor.prev
        return cursor.data





