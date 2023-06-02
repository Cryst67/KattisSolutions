test_case = input().split(' ')
[N, P, X, Y] = [int(x) for x in test_case]
curPage = 1
minutes = 0
while P != 0:
    if curPage % N == 0:
        minutes += Y
    else:
        minutes += X
        P-=1
    curPage += 1
if curPage % N == 0:
    minutes += Y
print(minutes)