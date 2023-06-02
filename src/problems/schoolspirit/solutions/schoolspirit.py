def get_score(l):
    s = 0
    for i in range(len(l)):
        s+= l[i] * (4/5)**i
    return 0.2 * s

n = int(input())
s = 0
l = []
scores = []
for i in range(n):
    score = int(input())
    l.append(score)
    s+= score * (4/5)**i
print(0.2*s)
for i in range(n):
    l_copy = l.copy()
    l_copy.remove(l[i])
    scores.append(get_score(l_copy))
print(sum(scores)/n)