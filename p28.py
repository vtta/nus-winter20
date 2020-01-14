
n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))

sum = 0
for i in range(k):
    sum += a[i]

print(sum)
