import sys
import functools
import itertools
import heapq
import collections


def main():
    t = int(input().strip())
    for i in range(t):
        queue = collections.deque()
        n = int(input().strip())
        for j in range(n):
            ops = input().strip().split()
            if ops[0] == "Count":
                print(len(queue))
            elif ops[0] == "In":
                queue.append(ops[1])
            elif ops[0] == "Out":
                print(queue.popleft() if len(queue) else "-1")


if __name__ == "__main__":
    main()
