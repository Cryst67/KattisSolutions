n = input()

for i in range(int(n)):
    s = input()
    s = s.split(' ')
    s = s[1:]
    s = [int(no) for no in s]
    for i in range(0, len(s) - 1):
        if s[i] != s[i + 1] - 1:
            print(i + 2)
            break
