v, e = map(int, input().split())
g = {}
for _ in range(e):
    frm, to = map(int, input().split())
    if frm not in g:
        g[frm] = {}
    if to not in g[frm]:
        g[frm][to] = 1
    else: g[frm][to] += 1

wl = int(input())
w = list(map(int, input().split()))
for i in range(wl):
    frm, to = w[i], w[i + 1]
    if frm not in g:
        print(i + 1)
        exit()
    if to not in g[frm]:
        print(i + 1)
        exit()
    else:
        if g[frm][to] == 0:
            print(i + 1)
            exit()
        else:
            g[frm][to] -= 1

if wl < e:
    print('too short')
    exit()
print('correct')