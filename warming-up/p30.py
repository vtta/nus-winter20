
tbl = [0]
for i in range(1, 200):
    tbl.append(tbl[i - 1] + i * i)

n = map(int, input().split(' '))
print(' '.join(map(lambda x: str(tbl[int(x)]), input().split(' '))))
