import sys
import math
import json
import functools
import itertools
import heapq
import collections


class Solver:
    def __init__(self):
        self.l = 4
        self.h = [1, 16, 256, 4096]
        self.t = [1, 12, 144, 1728]
        self.d = [1, 10, 100, 1000]
        self.ans = []

    def solve(self):
        for i in range(2992, 9999):
            h = 0
            t = 0
            d = 0
            for j in range(self.l):
                h += math.floor(i / self.h[j]) % 16
                t += math.floor(i / self.t[j]) % 12
                d += math.floor(i / self.d[j]) % 10
                # print(h, t, d)
            if h == t and t == d:
                self.ans.append(i)
                print(i)


def main():
    Solver().solve()


if __name__ == "__main__":
    main()