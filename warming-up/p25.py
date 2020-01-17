
a = input()
b = input()
c = input()

w = list(map(int, input().split(' ')))

if w[0]:
    a, b = b, a
if w[1]:
    b, c = c, b
if w[2]:
    a, c = c, a

print(a)
print(b)
print(c)
