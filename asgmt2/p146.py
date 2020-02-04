
def eratosthenes(n):
    is_prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(2, n + 1) if is_prime[x]]


MAXN = 1299709
primes = eratosthenes(MAXN)
gap = [0] * MAXN

for i in range(len(primes) - 1):
    l = primes[i]
    r = primes[i+1]
    d = r - l
    for j in range(l+1, r):
        gap[j] = d

if __name__ == "__main__":
    while True:
        n = int(input().strip())
        if n == 0:
            break
        print(gap[n])
