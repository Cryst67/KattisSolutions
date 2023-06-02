letters = list(set(list(input())))
d = {}
for i in range(int(input())):
    w = input()
    l = list(set(w))
    d[w] = l
for key in d:
    if len(key) < 4: continue
    flag = 1
    mid_letter = 0
    for letter in d[key]:
        if letter == letters[0]: mid_letter = 1
        if letter not in letters: flag = 0; break
    if flag and mid_letter: print(key)
