from ArrayStack import ArrayStack


class MaxStack:
    def __init__(self):
        self.data = ArrayStack()
        self.max_value = None

    def is_empty(self):
        return self.data.is_empty()

    def __len__(self):
        return len(self.data)

    def push(self, e):
        self.data.push((e, self.max_value))
        if self.max_value is None:
            self.max_value = e

        elif self.max_value < e:
            self.max_value = e

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.data.top()[0]

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        popped = self.data.pop()
        self.max_value = popped[1]
        return popped[0]

    def max(self):
        if self.max_value is None or self.is_empty():
            raise Exception('Stack is empty')
        return self.max_value



