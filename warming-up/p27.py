import itertools

l = []
for i in range(3):
    l.append(input())
s = input()

def solve():
    for i, j, k in itertools.product(range(3), range(3), range(3)):
        if l[i] + l[j] + l[k] == s:
            print("No")
            return False
    print("Yes")
    return False

solve()