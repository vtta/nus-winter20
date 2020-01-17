import cmath

a = int(input())
b = int(input())
c = int(input())

x = complex(a, b)
x = x**c
print(int(x.real))
print(int(x.imag))
