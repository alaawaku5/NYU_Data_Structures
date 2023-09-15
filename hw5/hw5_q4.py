from ArrayStack import ArrayStack


class Queue:
    def __init__(self):
        self.first = ArrayStack()
        self.second = ArrayStack()
        self.top = None
        self.n = len(self.first)+len(self.second)

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.n == 0

    def enqueue(self, elem):
        if self.is_empty():
            self.top = elem
        self.first.push(elem)
        self.n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elif self.second.is_empty():
            while not self.first.is_empty():
                self.second.push(self.first.pop())
        popped = self.second.pop()
        if not self.second.is_empty():
            self.top = self.second.top()
        else:
            self.top = None
        self.n -= 1
        while not self.second.is_empty():
            self.first.push(self.second.pop())
        return popped

    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.second.top




