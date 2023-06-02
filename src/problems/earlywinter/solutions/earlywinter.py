n, dm = map(int, input().split())
days = [*map(int, input().split())]
mini = dm
res = 0
for i in range(n):
    if days[i] > dm: res += 1
    else: break
    if i == n-1: print('It had never snowed this early!');exit()
print(f"It hadn't snowed this early in {res} years!")
