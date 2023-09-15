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

    def __iter__(self):
        for i in range(len(self)):
            yield self.data[i]  # could also yield self[i]

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
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.pop()


def stack_sum(s):
    if s.__len__() == 1:
        return s.top()
    last = s.pop()
    rest = stack_sum(s)
    stacksum = rest + last
    s.push(last)
    return stacksum


s = ArrayStack()
s.push(1)
s.push(2)
s.push(3)
# s.pop()
# print(s.top())
# print(s.__len__())
# print("sum", stack_sum(s))

a = [1, 2, 3]
a.reverse()


# print(a)


def eval_prefix(exp_str):
    exp_lst = exp_str.split()
    exp_lst.reverse()
    s = ArrayStack()

    for i in range(len(exp_lst)):
        s.push(exp_lst[i])

        if len(s) >= 3:
            first = s.pop()
            third = s.pop()
            second = s.pop()

            if first in "+-/*" and second.isdigit() and third.isdigit():
                if first == "+":
                    res = int(third) + int(second)
                elif first == "-":
                    res = int(third) - int(second)
                elif first == "*":
                    res = int(third) * int(second)
                elif first == "/":
                    res = int(int(third) / int(second))
                s.push(str(res))
            else:
                s.push(second)
                s.push(third)
                s.push(first)

    return s.top()


def eval_postfix(exp_str):
    exp_lst = exp_str.split()
    s = ArrayStack()

    for i in range(len(exp_lst)):
        s.push(exp_lst[i])

        if len(s) >= 3:
            first = s.pop()
            second = s.pop()
            third = s.pop()

            if first in "+-/*" and second.isdigit() and third.isdigit():
                if first == "+":
                    res = int(third) + int(second)
                elif first == "-":
                    res = int(third) - int(second)
                elif first == "*":
                    res = int(third) * int(second)
                elif first == "/":
                    res = int(int(third) / int(second))
                s.push(str(res))
            else:
                s.push(third)
                s.push(second)
                s.push(first)

    return s.top()

exp_str = "-3 2 *"
print(eval_postfix(exp_str))
a = "-3"
print(a.isdigit())

# q3
# lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
#
# [9,]
def flatten_list(lst):
    stack = ArrayStack()
    while len(lst) != 0:
        last = lst.pop()
        if isinstance(last, list):
            lst.extend(last)
        elif isinstance(last, int):
            stack.push(last)

    while not stack.is_empty():
        lst.append(stack.pop())
    return lst


lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
# print(flatten_list(lst))


# Optional
def stack_sort(s):
    helper_stack = ArrayStack()
    for iteration in range(len(s)):

        for i in range(len(s)):
            if len(s) == 1:
                helper_stack.push(s.pop())

            else:
                first = s.pop()
                second = s.pop()
                helper_stack.push(min(first, second))
                s.push(max(first, second))

        for i in range(len(helper_stack)):
            if len(helper_stack) == 1:
                s.push(helper_stack.pop())
            else:
                first = helper_stack.pop()
                second = helper_stack.pop()
                s.push(max(first, second))
                helper_stack.push(min(first, second))

s = ArrayStack()
s.push(2)
s.push(5)
s.push(7)
s.push(1)
s.push(0)
s.push(54)
s.push(-3)
s.push(42)
# print(stack_sort(s))
for i in range(len(s)):
    # print(s.top())
    s.pop()

