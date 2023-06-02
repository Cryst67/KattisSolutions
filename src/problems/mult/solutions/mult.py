t = int(input())
start = -1
start_flag = True
for i in range(t):
    n = int(input())
    if start_flag:
        start = n
        start_flag = False
        continue
    if n % start == 0:
        print(n)
        start_flag = True