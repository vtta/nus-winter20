
word = input()

wordlen = len(word)
palindrome = True

for i in range(int(wordlen / 2)):
    # print("l: {} r: {}".format(i, wordlen - i))
    if word[i] != word[wordlen - 1 - i]:
        palindrome = False
        break

if palindrome:
    print("Yes")
else:
    print("No")
