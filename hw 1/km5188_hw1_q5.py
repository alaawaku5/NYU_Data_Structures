def fibs(n):
    n1 = 1
    n2 = 1
    for i in range(n):
        yield n1
        n1, n2 = n2, n1 + n2


for curr in fibs(8):
    print(curr)
