
import itertools

n, k = map(int, input().split(' '))
stomach = list(map(int, input().split(' ')))
cake = list(map(int, input().split(' ')))

girls = list(map(lambda x: x[1], filter(
    lambda x: x[0] % 2 == 0, enumerate(stomach))))
boys = list(map(lambda x: x[1], filter(
    lambda x: x[0] % 2 == 1, enumerate(stomach))))

# print(stomach)
# print(cake)
# print(girls)
# print(boys)

who = []
girl = True
while cake != []:
    cur = cake.pop(0)
    if girl:
        for index, size in enumerate(girls):
            # print("girl cur: {} index: {} size:{}".format(cur, index, size))
            if cur <= size:
                who.append(2 * index + 1)
                girl = False
                break
    else:
        for index, size in reversed(list(enumerate(boys))):
            # print("boy cur: {} index: {} size:{}".format(cur, index, size))
            if cur <= size:
                who.append(2 * index + 2)
                girl = True
                break

list(map(print, who))
