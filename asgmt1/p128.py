
import sys


def fib(n):
    if(n < 2):
        return n
    x = 1
    y = 1
    mod = 1000000007
    for i in range(2, n):
        t = x + y
        x = y
        y = t % mod
    return y


if __name__ == "__main__":
    for line in sys.stdin:
        n = int(line.strip())
        print(fib(n))
