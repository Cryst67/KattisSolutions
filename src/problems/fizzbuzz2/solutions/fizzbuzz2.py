n, m = map(int, input().split())
fizz_buzz = []
for i in range(1, m + 1):
    s = ''
    if i % 3 == 0: s += 'fizz'
    if i % 5 == 0: s += 'buzz'
    if s == '': fizz_buzz.append(str(i))
    else: fizz_buzz.append(s)
maxi = [-1, float('-inf')]
for i in range(n):
    line = input().split()
    score = 0
    for j in range(m):
        if line[j] == fizz_buzz[j]: score += 1
    if score > maxi[1]:
        maxi = [i + 1, score]
print(maxi[0])