
cmds = """\
Alice and Bob swapped their paper.
Alice and Charlotte swapped their paper.
Bob and Alice swapped their paper.
Bob and Charlotte swapped their paper.
Alice erased the sentence on her paper.
Alice copied the sentence on Charlotte s paper to her paper.
Alice and Bob swapped their paper.
Charlotte and Bob swapped their paper.
Charlotte and Alice swapped their paper.\
"""

ids = [
    'Alice',
    'Bob',
    'Charlotte',
    'swapped',
    'copied',
    'erased',
]

paper = {
    'Alice': "",
    'Bob': "",
    'Charlotte': "",
}


def lex(line):
    output = []
    for i in line.split(' '):
        if i in ids:
            output.append(i)
    return output


def parse(tokens):
    last = tokens.pop()
    if last == "swapped":
        x = tokens.pop()
        y = tokens.pop()
        paper[x], paper[y] = paper[y], paper[x]
    elif last == "erased":
        paper[tokens.pop()] = ""
    else:
        tokens.pop()
        x = tokens.pop()
        paper[x] = paper[last]


def main():
    paper['Alice'] = input()
    paper['Bob'] = input()
    paper['Charlotte'] = input()
    for i in cmds.split('\n'):
        # print(i)
        x = lex(i)
        # print(x)
        parse(x)
    print(paper['Alice'])
    print(paper['Bob'])
    print(paper['Charlotte'])


if __name__ == "__main__":
    main()
