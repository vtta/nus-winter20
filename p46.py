import functools


def flip(x):
    return 1 ^ x


class Solver:
    def __init__(self, n, m, q):
        # n: number of rows
        # m: number of lights at each row
        # q: total number of operations need to be done
        self.n = n
        self.m = m
        self.q = q
        # Initially all lights are off
        self.lights = [[0 for i in range(m)] for i in range(n)]
        # how many lights are on in a row
        self.cnt = [0 for i in range(n)]
        # which status indicates that the lights are on
        self.on = [1 for i in range(n)]
        # total on count
        self.total = 0

    def is_on(self, x, y):
        return self.lights[x][y] == self.on[x]

    def is_off(self, x, y):
        return not self.is_on(x, y)

    def set_on(self, x, y):
        if self.is_off(x, y):
            self.lights[x][y] = self.on[x]
            self.cnt[x] += 1
            self.total += 1

    def set_off(self, x, y):
        if self.is_on(x, y):
            self.lights[x][y] = flip(self.on[x])
            self.cnt[x] -= 1
            self.total -= 1

    def switch(self, x):
        on = self.cnt[x]
        off = self.m - on
        self.total -= on
        self.total += off
        self.cnt[x] = off
        self.on[x] = flip(self.on[x])

    def solve(self):
        for i in range(self.q):
            ops = list(map(int, input().strip().split(' ')))
            op = ops[0]
            # Turn the y-th light at x-th row on if it is off
            if op == 1:
                x, y = map(lambda x: x - 1, ops[1:])
                self.set_on(x, y)
            # Turn the y-th light at x-th row off if it is on
            elif op == 2:
                x, y = map(lambda x: x - 1, ops[1:])
                self.set_off(x, y)
            # Switch all the lights at x-th row
            else:
                self.switch(ops[1] - 1)
            print(self.total)


def main():
    n, m, q = map(int, input().strip().split(' '))
    Solver(n, m, q).solve()


if __name__ == "__main__":
    main()
