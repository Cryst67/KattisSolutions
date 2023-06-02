n, e = map(int, input().split())
ppl = 0
reject = 0
for i in range(e):
    event, peeps = input().split()
    if event == 'enter':
        if int(peeps) + ppl > n:
            reject += 1
        else:
            ppl += int(peeps)
    else:
        ppl -= int(peeps)
print(reject)
