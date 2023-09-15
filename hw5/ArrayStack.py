import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

from ArrayList import ArrayList


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
        if(self.is_full()):
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
        if(self.is_empty()):
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
