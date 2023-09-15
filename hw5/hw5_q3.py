from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque


class MidStack:
    def __init__(self):
        self.first = ArrayStack()
        self.second = ArrayDeque()
        self.n = len(self.first) + len(self.second)

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self.n

    def push(self, e):
        self.n += 1
        if self.is_empty():
            self.first.push(e)
        else:
            self.second.enqueue_first(e)

    def top(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        elif self.second.is_empty():
            return self.first.top()
        else:
            return self.second.first()

    def pop(self):
        if self.is_empty():
            raise Exception("MidStack is empty")
        elif self.second.is_empty():
            self.n -= 1
            return self.first.pop()
        else:
            self.n -= 1
            return self.second.dequeue_first()

    def mid_push(self, e):
        if not self.is_empty():
            while (len(self)//2) != len(self.second):
                self.first.push(self.second.dequeue_last())
            self.first.push(e)
        elif self.is_empty():
            self.first.push(e)
        self.n += 1