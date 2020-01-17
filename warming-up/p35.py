
def predicate(x):
    return (x % 3 != 0) and (x % 5 != 0) and ('3' not in str(x)) and ('5' not in str(x))


n, k = map(int, input().strip().split(' '))
list(map(print, list(filter(predicate, range(1, n + 1)))[:k]))
