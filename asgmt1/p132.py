import sys
import functools
import itertools
import heapq
import collections


def main():
    # m份礼物中选择n份
    n, m = map(int, input().strip().split())
    lst = list(map(int, input().strip().split()))
    lst.sort()
    res = lst[-1] - lst[0]
    for i in range(m - n + 1):
        begin = i
        end = i + n - 1
        res = min(res, lst[end] - lst[begin])
    print(res)


if __name__ == "__main__":
    k = int(input().strip())
    for i in range(k):
        main()

# 5 7 10 10 12 22
