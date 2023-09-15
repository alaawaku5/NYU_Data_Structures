def a(n):
    res = 0
    for integer in range(n):
        res += integer ** 2
    return res


def b(n):
    return sum([integer ** 2 for integer in range(n)])


def c(n):
    res = 0
    for integer in range(n):
        if integer % 2 != 0:
            res += integer ** 2
    return res


def d(n):
    return sum([integer ** 2 for integer in range(n) if integer % 2 != 0])
