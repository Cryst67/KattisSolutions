s = input()
d = {}
for letter in s:
    if letter not in d:
        d[letter] =True
        continue
    else:
        print(0)
        exit()

print(1)