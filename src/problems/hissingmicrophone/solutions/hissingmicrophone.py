s = input()

for i in range(len(s)):
    if i == len(s) - 1:
        break
    if s[i] == 's':
        if s[i + 1] == 's':
            print('hiss')
            exit()

print('no hiss')