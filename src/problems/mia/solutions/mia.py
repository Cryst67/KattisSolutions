def getScore(a, b):
    if b > a: 
        temp = a
        a = b
        b = temp
    if a == 2 and b == 1: return 1000000
    if a == b: return b * 100
    return a * 10 + b
while True:
    s0, s1, r0, r1 = map(int, input().split())
    if s0 == s1 == r0 == r1 == 0: break
    p1 = getScore(s0, s1)
    p2 = getScore(r0, r1)
    if p1 == p2: print('Tie.')
    elif p1 > p2: print('Player 1 wins.')
    else: print('Player 2 wins.')
    