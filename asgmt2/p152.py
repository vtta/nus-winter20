
import heapq

# just a wrapper
class Heap:
    def __init__(self, lst=None):
        if lst:
            heapq.heapify(lst)
            self.heap = lst
        else:
            self.heap = []

    def push(self, x):
        return heapq.heappush(self.heap, x)

    def pop(self):
        return heapq.heappop(self.heap)

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)


def main():
    # n is the number of tasks
    # m is the number of direct precedence relations between tasks
    #   task i must be executed before task j
    n, m = map(int, input().strip().split(' '))
    adj = [[] for i in range(n)]
    ind = [0 for i in range(n)]
    res = []

    def topo():
        pq = Heap()
        for i in range(n):
            if ind[i] == 0:
                pq.push(i)
        # print(pq)
        while pq:
            u = pq.pop()
            res.append(u)
            for i in adj[u]:
                ind[i] -= 1
                if ind[i] == 0:
                    pq.push(i)

    for _ in range(m):
        i, j = map(int, input().strip().split(' '))
        adj[i-1].append(j-1)
        ind[j-1] += 1

    topo()
    print(' '.join(map(lambda x: str(x + 1), res)))
    # output the smallest one by lexical order


if __name__ == "__main__":
    T = int(input().strip())
    for i in range(T):
        main()
