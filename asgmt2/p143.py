
import sys


def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    b = float(input().strip())
    r, v, e, f = map(float, input().strip().split(' '))

    def h(x):
        if x >= r:
            return 1.0/(v - e * (x - r))
        else:
            return 1.0/(v - f * (r - x))

    a.insert(0, 0)
    cost = [0] * (a[n] + 1)
    for i in range(1, a[n] + 1):
        cost[i] = h(i - 1) + cost[i - 1]
    f = [0] * (n + 1)

    for i in range(1, n + 1):
        t = sys.maxsize
        for j in range(i):
            t = min(t, f[j] + cost[a[i] - a[j]] + b)
        f[i] = min(t, cost[a[i]])

    print("{:.4f}".format(f[n]))


if __name__ == "__main__":
    while True:
        try:
            main()
        except EOFError:
            break
