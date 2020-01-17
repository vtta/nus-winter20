
s = input().strip()
l = int(input().strip())
w = input().strip()

s = s.split(' ')
s = s[l:]
if s:
    print(s.count(w))
else:
    print(0)
