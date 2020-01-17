
n = int(input())
a, b, c = map(int, input().split(' '))

tbl = [0, a, b, c]
for i in range(4, n + 1):
    tbl.append(a * tbl[i - 1] + b * tbl[i - 2] + c * tbl[i - 3])
print(tbl[n])
