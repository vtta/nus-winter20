import heapq as hq

n = int(input())

h = []
for i in range(n):
    op, r = map(int, input().split(' '))
    # buy a bread with radius at least r
    if op == 1:
        if h == []:
            print(-1)
            continue
        
        largest = -h[0]
        if largest < r:
            print(-1)
        else:
            print(largest)
            hq.heappop(h)
    # baker make a new bread with radius r
    elif op == 2:
        hq.heappush(h, -r)
