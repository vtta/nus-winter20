

if __name__ == "__main__":
    while True:
        n = int(input().strip())
        if n == 0:
            break
        if n % 2:
            print('Bob')
        else:
            print('Alice')
