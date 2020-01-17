
tokens = input().strip().split(' ')
opd = []
while tokens:
    last = tokens.pop()
    if last == '':
        continue
    elif last == '-':
        opd.append(opd.pop() - opd.pop())
    elif last == '+':
        opd.append(opd.pop() + opd.pop())
    elif last == '*':
        opd.append(opd.pop() * opd.pop())
    else:
        opd.append(int(last))

print(opd.pop())
