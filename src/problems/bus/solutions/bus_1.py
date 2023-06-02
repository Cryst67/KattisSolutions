n = int(input())
for i in range(n):
    k = int(input())
    ppl = 0
    while k != 0:
        ppl = (ppl*2)+1
        k-=1
    print(ppl)