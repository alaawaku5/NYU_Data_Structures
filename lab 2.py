# Coding
# Question 1

class Polynomial:
    def __init__(self, data):
        self.data = data
        self.reversed = self.data[::-1]

    def __add__(self, other):
        new_pol = [] * (len(self.data))
        for i in range(len(self.data)):
            new_pol.append(self.data[i] + other.data[i])
        return Polynomial(new_pol)

    def __call__(self, param):
        call = 0
        for i in range(len(self.data)):
            call += self.reversed[i] * (param ** (len(self.data) - i - 1))
        return call

    def __repr__(self):
        repr_lst = []
        for i in range(len(self.data)):
            repr_lst.append("{a}x^{b}".format(a=self.reversed[i], b=len(self.data) - i - 1))
        return '+'.join(repr_lst)

    def __mul__(self, other):
        new_lst = ["0"] * (len(self.data) + len(other.data) - 1)
        for i in range(len(self.data)):
            for j in range(len(other.data)):
                new_index = i + j
                new_lst[new_index] = int(new_lst[new_index]) + (self.data[i] * other.data[j])

        return Polynomial(new_lst)

    def __derive__(self):
        pass


p1 = Polynomial([1, 2, 3])
p2 = Polynomial([1, 1])
# p3 = p1 + p2
p4 = p1 * p2
# print(p1(1))


# Question 2
def powers_of_two(n):
    for i in range(n):
        yield 2 ** i


# for i in powers_of_two(6):
#     print(i)


# Question 3

class UnsignedBinaryInteger:

    def __init__(self, bin_num_str):
        self.data = bin_num_str
        self.arr = [int(x) for x in bin_num_str]

    def decimal(self):
        dec = 0
        for ind in range(len(self.arr)):
            rev_ind = -(ind-(len(self.arr)-1))
            dec += (2**ind)*self.arr[rev_ind]
        return dec

    def __lt__(self, other):
        return self.decimal() < other.decimal()

    def __gt__(self, other):
        return self.decimal() > other.decimal()

    def __eq__(self, other):
        return self.decimal() == other.decimal()

    def is_twos_power(self):
        return self.arr[0] == 1 and self.arr.count(0) == len(self.data)-1

    def largest_twos_power(self):
        return len(self.arr)-1

    def __repr__(self):
        return "0b"+str(self.data)


n = UnsignedBinaryInteger("1101")

print(n.is_twos_power())

# optional vitamins
# 5
print([(-2)**i for i in range(8)])

print(["1"*i for i in range(1,8)])

# 6
my_str = "Java"
print([i for i in my_str*2])
