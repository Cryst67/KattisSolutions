s = input()
a = 0
b = 0
for i in range(len(s)):
     if s[i] == 'A': a+=1
     if s[i] == 'B': b+=1
l = max(a, b)
aw = []
for i in range(1, l +1):
    a_wins = 0
    b_wins = 0
    a, b = 0, 0
    for letter in s:
        if letter == 'A': a += 1
        if letter == 'B': b += 1
        if a == i: 
            a_wins += 1
            a, b = 0, 0
        if b == i:
            b_wins += 1
            a, b = 0, 0
    if a_wins > b_wins: aw.append(i)
print(len(aw))
print(' '.join(map(str, aw)))