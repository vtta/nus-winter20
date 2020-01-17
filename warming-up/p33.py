
import math

l = 1000
tbl = [True] * l
for i in range(2, int(math.sqrt(l) + 1)):
    for j in range(i * 2, l, i):
        tbl[j] = False

n = int(input())

sum = 0
cnt = 0
for i in range(2, l):
    if tbl[i]:
        sum += i
        cnt += 1
        if sum >= n:
            print(cnt)
            break
