
n, k = map(int, input().split(' '))

goods = []
cnt = []

for i in range(n):
    ops = input()
    if ops[0] == '1':
        if goods == []:
            print('?')
            continue
        print(goods.pop())
    else:
        op, x = map(int, ops.split(' '))
        goods.append(x)
