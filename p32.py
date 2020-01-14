
tbl = [
    ["******", "*    *", "*    *", "*    *", "*    *", "*    *", "******", ],
    ["*", "*", "*", "*", "*", "*", "*", ],
    ["******", "     *", "     *", "******", "*     ", "*     ", "******", ],
    ["******", "     *", "     *", "******", "     *", "     *", "******", ],
]

n = int(input())
s = list(map(int, input().split(' ')))

res = [""]*7
for j in range(7):
    res[j] += tbl[s[0]][j]

for i in s[1:]:
    for j in range(7):
        res[j] += "  "
        res[j] += tbl[i][j]

for j in range(7):
    print(res[j])
