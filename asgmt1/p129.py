
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    def __str__(self):
        return str(self.val)


class List():
    def __init__(self):
        self.head = None

    # insert after
    def insert(self, pos=None, val=None):
        if pos:
            r = pos.right
            new = Node(val, pos, r)
            pos.right = new
            if r:
                r.left = new
                return new
        else:
            self.head = Node(val)
            self.head.left = self.head
            self.head.right = self.head
            return self.head

    def erase(self, pos):
        if pos.right == pos and pos.left == pos:
            self.head = None
            return pos
        r = pos.right
        l = pos.left
        l.right = r
        r.left = l
        return pos

    def empty(self):
        return self.head is None


def solve(n, m):
    l = List()
    pos = None
    for i in range(n):
        pos = l.insert(pos, i + 1)
    pos = l.head
    while True:
        for i in range(m):
            #print(pos.val, end=' ')
            if i == m - 1:
                pos = l.erase(pos)
                if l.empty():
                    print(pos.val)
                    return
            pos = pos.right


if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        # n monkey, m number
        n, m = map(int, input().strip().split())
        solve(n, m)
