import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        return self.data[ind]

    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        self.data[ind] = val

    def pop(self, ind=-1):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        elem = self.data[ind]
        for i in range(ind + 1, self.n):
            self.data[i - 1] = self.data[i]
        self.data[self.n - 1] = None
        self.n -= 1
        if (self.n < self.capacity // 4):
            self.resize(self.capacity // 2)
        return elem

    def insert(self, ind, value):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        for j in range(self.n, ind, -1):
            self.data[j] = self.data[j - 1]
        self.data[ind] = value
        self.n += 1

    def __repr__(self):
        data_as_strings = [str(self.data[i]) for i in range(self.n)]
        return '[' + ', '.join(data_as_strings) + ']'

    def __add__(self, other):
        res = ArrayList()
        res.extend(self)
        res.extend(other)
        return res

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, times):
        res = ArrayList()
        for i in range(times):
            res.extend(self)
        return res

    def __rmul__(self, times):
        return self * times


class StaticArrayStack:
    def __init__(self, max_capacity):
        self.data = make_array(max_capacity)
        self.capacity = max_capacity
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def is_full(self):
        return (len(self) == self.capacity)

    def push(self, item):
        if (self.is_full()):
            raise Exception("Stack is full")
        self.data[self.n] = item
        self.n += 1

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        item = self.data[self.n - 1]
        self.data[self.n - 1] = None
        self.n -= 1
        return item

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[self.n - 1]


class ArrayStack:
    def __init__(self):
        self.data = ArrayList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.pop()


class ArrayDeque:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data = make_array(ArrayDeque.INITIAL_CAPACITY)
        self.num_of_elems = 0
        self.front_ind = None
        self.back_ind = None

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue_first(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        if (self.is_empty()):
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems = 1
        else:
            self.front_ind = (self.front_ind - 1) % len(self.data)
            self.data[self.front_ind] = elem
            self.num_of_elems += 1

    def enqueue_last(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        if (self.is_empty()):
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems = 1
        else:
            self.back_ind = (self.back_ind + 1) % len(self.data)
            self.data[self.back_ind] = elem
            self.num_of_elems += 1

    def dequeue_first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.is_empty()):
            self.front_ind = None
            self.back_ind = None
        elif (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def dequeue_last(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.back_ind]
        self.data[self.back_ind] = None
        self.back_ind = (self.back_ind - 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.is_empty()):
            self.front_ind = None
            self.back_ind = None
        elif (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.back_ind]

    def resize(self, new_cap):
        old_data = self.data
        new_data = make_array(new_cap)
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            new_data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.data = new_data
        self.front_ind = 0
        self.back_ind = self.front_ind + self.num_of_elems - 1


# q1
# def postfix_calc(prompt):
#


# q2
class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.max_value = ArrayStack()

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

    def push(self, e):
        if self.max_value.is_empty() or self.max_value.top() < e:
            self.max_value.push(e)
        self.data.push(e)

    def top(self):
        return self.data.top()

    def pop(self):
        if self.max_value.top() == self.data.top():
            self.max_value.pop()
        return self.data.pop()

    def max(self):
        return self.max_value.top()


# q3
class MidStack:
    def __init__(self):
        self.data = ArrayDeque()
        self.data2 = ArrayStack()

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

    def push(self, e):
        self.data.enqueue_last(e)

    def top(self):
        return self.data.last()

    def pop(self):
        return self.data.dequeue_last()

    def mid_push(self, e):
        print(self.data.front_ind, self.data.back_ind)
        mid = len(self) // 2
        self.data.front_ind = (self.data.front_ind + mid) % len(self)
        self.data.back_ind = (self.data.back_ind - mid - len(self) % 2) % len(self)

        # print(self.data.front_ind, self.data.back_ind)
        self.data.enqueue_last(e)
        # print(self.data.front_ind, self.data.back_ind)
        self.data.front_ind = (self.data.front_ind - mid) % len(self)
        self.data.back_ind = (self.data.back_ind + mid) % len(self)
        print(self.data.front_ind, self.data.back_ind)


mids = MidStack()
mids.push(2)
# print(mids.top())
mids.push(4)
mids.push(6)
mids.push(8)
mids.mid_push(10)
print(mids.pop())
mids.mid_push(10)
print(mids.data.back_ind)

# mids.top()
a = ArrayStack()
a.push(2)


# print(a.top())


class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.max_value = ArrayStack()

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

    def push(self, e):
        if self.max_value.is_empty() or self.max_value.top() < e:
            self.max_value.push(e)
        self.data.push(e)

    def top(self):
        return self.data.top()

    def pop(self):
        if self.max_value.top() == self.data.top():
            self.max_value.pop()
        return self.data.pop()

    def max(self):
        return self.max_value.top()


maxS = MaxStack()
maxS.push(3)
maxS.push(1)
maxS.push(6)
maxS.push(4)
print(maxS.max())
print(maxS.pop())
print(maxS.pop())
print(maxS.max())



class MidStack:
    def __init__(self):
        self.data = ArrayStack()

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

    def push(self, e):
        self.data.push(e)

    def top(self):
        return self.data.top()

    def pop(self):
        return self.data.pop()

    def mid_push(self, e):
        pass
