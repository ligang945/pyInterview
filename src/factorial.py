def f(x):
    if x == 1:
        return 1
    else:
        return x * f(x - 1)

print(f(5))

from functools import reduce


def g(x):
    return reduce(lambda a, b: a * b, range(1, x + 1))

print(g(5))


def prod(x, y):
    return x * y

print(reduce(prod, [2, 4, 5, 7, 12]))
