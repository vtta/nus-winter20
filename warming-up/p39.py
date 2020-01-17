import math
import functools

l = 200
primes = [True] * l
squares = [False] * l
for i in range(2, int(math.sqrt(l) + 1)):
    for j in range(i * 2, l, i):
        primes[j] = False
for i in range(int(math.sqrt(l) + 1)):
    squares[i * i] = True


def f(x):
    if x == 1:
        return 10
    if primes[x]:
        return x * x
    if squares[x]:
        return 2 * int(math.sqrt(x)) + 1
    return int(math.sqrt(x))


n = int(input())
print(functools.reduce(lambda x, y: x + f(y), range(1, n + 1), 0))
