import sys
import functools
import itertools
import heapq
import collections


class Solver:
    def __init__(self, col, code):
        self.col = col
        self.code = code
        self.ans = ""
        self.row = int(len(self.code)/self.col)
        self.m = [['x' for j in range(self.col)] for i in range(self.row)]
        # print(self.code, len(self.code))

    def solve(self):
        for y in range(self.row):
            for x in range(self.col):
                pos = y * self.col + (x if y % 2 == 0 else self.col - x - 1)
                self.m[y][x] = self.code[pos]
                # print(y, x, pos)
        # print(self.m)
        for x in range(self.col):
            for y in range(self.row):
                print(self.m[y][x], end='')
        print()


def main():
    n = int(input().strip())
    if n == 0:
        return
    s = input().strip()
    Solver(n, s).solve()


if __name__ == "__main__":
    while True:
        try:
            main()
        except EOFError:
            break
