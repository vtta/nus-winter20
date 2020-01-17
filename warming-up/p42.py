
a, b = map(int, input().split(' '))
while a != b:
    if a > b:
        a = int(a / 2)
    else:
        b = int(b / 2)
print(a)
