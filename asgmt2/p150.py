import string
digs = string.digits + string.ascii_letters


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)


def main():
    m = int(input().strip())
    a = int(input().strip(), m)
    b = int(input().strip(), m)
    p = int(a / b)
    q = a % b
    print(int2base(p, m).upper())
    print(int2base(q, m).upper())


if __name__ == "__main__":
    T = int(input().strip())
    for i in range(T):
        main()
