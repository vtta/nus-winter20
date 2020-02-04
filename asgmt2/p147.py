T = int(input().strip())
for i in range(T):
    pos, word = input().strip().split(' ')
    pos = int(pos)
    print(i + 1, word[0:pos-1]+word[pos:])
