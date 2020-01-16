
n = int(input())
tbl = [0, 1]
for i in range(2, n + 1):
    if i % 2 == 0:
        tbl.append(tbl[int(i / 2)])
    else:
        tbl.append(tbl[i - 1] + 1)

print(tbl[n])
