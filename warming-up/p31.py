
import math

l = 200
tbl = [True] * l
for i in range(2, int(math.sqrt(l) + 1)):
    for j in range(i * 2, l, i):
        tbl[j] = False

n = int(input())
s = 0
for i in range(2, n + 1):
    if tbl[i]:
        s += 1

print(s)
