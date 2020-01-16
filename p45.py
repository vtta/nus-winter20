
n, d = map(int, input().split(' '))
# maximal storage of each type of goods
b = list(map(int, input().split(' ')))
b.insert(0, 0)
# current storage of each type of goods
a = list(map(int, input().split(' ')))
a.insert(0, 0)

for i in range(d):
    for j in range(5):
        op, x, y = map(int, input().split(' '))
        # The person wants to sell y many x-th type of goods to you.
        if op == 1:
            a[x] = min([b[x], a[x] + y])

        # The person wants to buy y many x-th type of goods from you.
        if op == 2:
            if y <= a[x]:
                a[x] -= y

    print(' '.join(map(str, a[1:])))
