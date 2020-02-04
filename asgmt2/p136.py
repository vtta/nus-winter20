import sys
import functools
import itertools
import heapq
import collections
import math


class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v

    def __lt__(self, other):
        return self.k < other.k or (self.k == other.k and self.v < other.v)


class Solver:
    def __init__(self, key, text):
        self.key = key
        self.text = text

        seq = []
        for i, c in enumerate(key):
            seq.append(Node(c, i))
        seq.sort()

        self.seq = []
        for i in seq:
            self.seq.append(i.v)
        # print(self.seq)

        self.col = len(key)
        self.row = int(len(text) / len(key))
        self.map = [['X' for i in range(self.col)]
                    for j in range(self.row)]
        # print(self.map)

    def solve(self):
        cur = 0
        for i in self.seq:
            for j in range(self.row):
                self.map[j][i] = self.text[cur]
                cur += 1
        for j in range(self.row):
            for i in range(self.col):
                print(self.map[j][i], end='')
        print()


def main():
    key = input().strip()
    if key == "THEEND":
        return
    text = input().strip()
    Solver(key, text).solve()


if __name__ == "__main__":
    while True:
        try:
            main()
        except EOFError:
            break
