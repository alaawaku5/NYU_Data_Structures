
from math import sqrt, ceil, floor


def factors(num):
    end = int(sqrt(num))
    for i in range(1, end + 1):
        if num % i == 0:
            yield i

    if ceil(sqrt(num)) != floor(sqrt(num)):
        end += 1

    for i in reversed(range(1, end)):
        if num % i == 0:
            yield num // i
