
def eratosthenes(n):
    is_prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [x for x in range(2, n + 1) if is_prime[x]]


MAXN = 1299709
primes = eratosthenes(MAXN)

n = int(input().strip())
print(primes[n - 1])
