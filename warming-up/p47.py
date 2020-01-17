# O(n) cyclic linked list


class Node(object):
    def __init__(self, data, left=0, right=0):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "({}, {}, {})".format(self.left, self.data, self.right)


class Solver:
    def __init__(self, ops):
        self.ops = ops
        self.elems = [Node('^')]
        # last valid node
        self.cur = 0
        self.trash = []

    def traverse(self):
        buf = ''
        cur = self.elems[0].right
        while cur != 0:
            buf += self.elems[cur].data
            cur = self.elems[cur].right
        return '?' if buf == '' else buf

    def delete(self, index):
        x = self.elems[index]
        l = self.elems[x.left]
        r = self.elems[x.right]
        l.right = x.right
        r.left = x.left
        self.trash.append(index)
        return x.left

    def new(self, value, left=0, right=0):
        if self.trash:
            index = self.trash.pop()
            self.elems[index] = Node(value, left, right)
            return index
        self.elems.append(Node(value, left, right))
        return len(self.elems) - 1

    # insert value after index
    # return new cursor position
    def insert(self, index, value):
        x = self.elems[index]
        # l = self.elems[x.left]
        r = self.elems[x.right]
        cur = self.new(value, index, x.right)
        r.left = cur
        x.right = cur
        return cur

    # cyclic linked list
    def end(self):
        return self.elems[0].left

    def begin(self):
        return 0

    def solve(self):
        cur = 0
        for v in self.ops:
            if v == '[':
                cur = self.begin()
            elif v == ']':
                cur = self.end()
            elif v == '<':
                if cur != self.begin():
                    x = self.elems[cur]
                    cur = x.left
            elif v == '>':
                x = self.elems[cur]
                r = x.right
                if r != self.begin():
                    cur = r
            elif v == '-':
                if cur != self.begin():
                    cur = self.delete(cur)
            else:
                cur = self.insert(cur, v)
            # list(map(lambda x: print(x, end=' '), self.elems))
            # print()
        print(self.traverse())


def main():
    Solver(input().strip()).solve()


if __name__ == "__main__":
    main()
