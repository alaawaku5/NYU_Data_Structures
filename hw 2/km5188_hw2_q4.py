def e_approx(n):
    e = 0
    term = 1
    for i in range(n + 1):
        e += term
        term /= i + 1
    return e
