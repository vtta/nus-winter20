# run-error
from collections import deque

n, k = map(int, input().strip().split(' '))
goods = deque()
# top    == right
# bottom == left
for i in range(n):
    ops = input()
    # drop out the gift at the bottom
    if ops[0] == '1':
        if goods:
            print(goods.popleft())
        else:
            print('?')
    # shuffle: if the machine is not empty, it will move a gift from the top and insert it at the bottom.
    elif ops[0] == '3':
        if goods:
            goods.appendleft(goods.pop())
    #  refill a gift of type x at the top
    else:
        op, x = map(int, ops.split(' '))
        goods.append(x)
