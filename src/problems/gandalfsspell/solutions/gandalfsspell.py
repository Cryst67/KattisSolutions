letters = input()
words = input().split()
if len(letters) != len(words): print(False); exit()
d = {}
l = {}
for i in range(len(words)):
    letter = letters[i]
    word = words[i]
    if word not in d:
        d[word] = letter
    else:
        if d[word] != letter:
            print(False)
            exit()
    if letter not in l:
        l[letter] = word
    else:
        if l[letter] != word:
            print(False)
            exit()
print(True)