n = int(input())
wins = n
for _ in range(n):
    s = input()
    for i in range(len(s) - 1):
        if s[i] == 'C' and s[i+1] == 'D':
            wins -=1
            break
print(wins)