
import itertools

n, k = map(int, input().strip().split(' '))
names = input().strip().split(' ')
records = list(map(float, input().strip().split(' ')))

for i in range(k):
    l, r = map(int, input().strip().split(' '))
    l = max([l, 1])
    r = min([r, n])
    cnt = {}
    grades = {}
    for j in range(l - 1, r):
        name = names[j]
        cnt[name] = cnt.get(name, 0) + 1
        grades[name] = grades.get(name, 0) + records[j]
    total = 0
    people = 0
    for name in grades.keys():
        people += 1
        total += grades[name] / cnt[name]
    print(total / people)
