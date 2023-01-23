import sys

sys.setrecursionlimit(1600)

cache = dict()


def fib(n):
    global cache
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = fib(n - 1) + fib(n - 2)
    return cache[n]


def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(100))
print(fib2(100))
