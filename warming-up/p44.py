

n = int(input().strip())
mat = [[0 for i in range(n)] for i in range(n)]
s = input().strip()


def solve(cur, sz, x, y):
    if sz == 1:
        mat[x][y] = int(s[cur])
        return cur + 1
    elif s[cur] == "D":
        cur = cur + 1
        sz = int(sz / 2)
        cur = solve(cur, sz, x, y)
        cur = solve(cur, sz, x, y + sz)
        cur = solve(cur, sz, x + sz, y)
        cur = solve(cur, sz, x + sz, y + sz)
        return cur
    elif s[cur] == "1":
        for i in range(x, x + sz):
            for j in range(y, y + sz):
                mat[i][j] = 1
        return cur + 1
    else:
        return cur + 1


solve(0, n, 0, 0)
list(map(lambda line: print(' '.join(map(str, line))), mat))
