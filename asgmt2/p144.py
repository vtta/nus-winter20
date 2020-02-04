
import sys

INVALID = -1


def main():
    n = int(input().strip())
    w = list(map(int, input().strip().split(' ')))

    w.extend(w)
    w.append(w[0])
    dp = [[INVALID for j in range(len(w))] for i in range(len(w))]
    for i in range(1, len(w)):
        dp[i-1][i] = 0
    # print(w, dp)

    def f(i, j):
        if dp[i][j] != INVALID:
            return dp[i][j]
        m = INVALID
        for k in range(i + 1, j):
            m = max(m, f(i, k) + f(k, j) + w[i]*w[k]*w[j])
        dp[i][j] = m
        return m

    res = INVALID
    for i in range(n):
        res = max(res, f(i, i + n))
    print(res)


if __name__ == "__main__":
    while True:
        try:
            main()
        except EOFError:
            break
