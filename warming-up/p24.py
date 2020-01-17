
# 1. At least one of the following statement is false:
# (a) The bitwise AND of a1 and a2 is less than or equal to a5.
# (b) The summation of a3 and a4 is more than a5.
# 2. All of the following statements are true:
# (a) The bitwise OR of a3 and a4 is less than a1
# (b) The product of a4 and a5 is more than or equal to a1.

a1, a2, a3, a4, a5 = map(int, input().strip().split(' '))
b1 = ((a1 & a2) > a5) or (a3 + a4 <= a5)
b2 = ((a3 | a4) < a1) and (a4 * a5 >= a1)
res = (not b1) and (not b2)
print(res)
