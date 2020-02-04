

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.weight = 0
        self.end = False

    # return value indicates that inserted value doesn't match any existing prefix
    def add(self, word):
        unique = True
        node = self
        for char in word:
            match = False
            for child in node.children:
                if child.char == char:
                    if child.end:
                        unique = False
                    child.weight += 1
                    node = child
                    match = True
                    break
            if not match:
                new = TrieNode(char)
                node.children.append(new)
                node = new
        node.end = True
        return unique and not node.children


def main():
    l = []
    n = int(input().strip())
    for i in range(n):
        l.append(input().strip())
    trie = TrieNode('$')
    for i in l:
        unique = trie.add(i)
        if not unique:
            print('NO')
            return
    print('YES')


if __name__ == "__main__":
    T = int(input().strip())
    for i in range(T):
        main()
