

def detach(x):
    l = x.l
    r = x.r
    r.l = l
    l.r = r

# 把小球X移动到小球Y的左边
def left(x, y):
    detach(x)
    l = y.l
    l.r = x
    x.l = l
    x.r = y
    y.l = x

# 把小球X移动到小球Y右边
def right(x, y):
    detach(x)
    r = y.r
    r.l = x
    x.r = r
    x.l = y
    y.r = x


class Node:
    def __init__(self, x):
        self.l = None
        self.r = None
        self.x = x


def main():
    n, m = map(int, input().strip().split(' '))
    balls = [Node(i) for i in range(n+1)]
    for i in range(n+1):
        balls[i].l = balls[(i-1) % (n+1)]
        balls[i].r = balls[(i+1) % (n+1)]
    for i in range(m):
        op, x, y = map(int, input().strip().split(' '))
        if op == 1:
            left(balls[x], balls[y])
        else:
            right(balls[x], balls[y])
    b = balls[0].r
    while b != balls[0]:
        print(b.x, end=' ')
        b = b.r
    print()


if __name__ == "__main__":
    T = int(input().strip())
    for i in range(T):
        main()
