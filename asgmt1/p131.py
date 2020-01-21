
import sys
import functools
import itertools
import heapq
import collections


class Node:
    def __init__(self, i, c, m, e):
        self.i = i
        self.c = c
        self.m = m
        self.e = e

    def total(self):
        return self.c + self.m + self.e

    def __lt__(self, other):
        if (self.total() > other.total()):
            return True
        if (self.total() == other.total()):
            if self.c > other.c:
                return True
            elif self.c == other.c:
                return self.i < other.i
        return False

    def __str__(self):
        return "{} {}".format(self.i, self.total())


def main():
    while True:
        n = int(input().strip())
        lst = []
        for i in range(n):
            c, m, e = map(int, input().strip().split())
            lst.append(Node(i + 1, c, m, e))
        lst.sort()
        for i in range(5):
            print(str(lst[i]))
        print()


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        pass
