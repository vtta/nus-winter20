import sys

squares = set()
for i in range(100):
    squares.add(i * i)

for x in sys.stdin:
    print(int(x) in squares)
