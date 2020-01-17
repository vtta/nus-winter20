import math

a = int(input())
b = int(input())
c = int(input())
delta = math.sqrt(b * b - 4 * a * c)
x1 = (-b - delta) / (2 * a)
x2 = (-b + delta) / (2 * a)
print(x1)
print(x2)
