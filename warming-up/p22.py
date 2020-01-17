
vec = list(map(int, input().split()))
# For Bob’s and Charlotte’s exam, at least one of these 2 exams you must score at least 60.
# For Alice’s exam you must score more than 60.
print((vec[1] >= 60 or vec[2] >= 60) and vec[0] >= 60)
