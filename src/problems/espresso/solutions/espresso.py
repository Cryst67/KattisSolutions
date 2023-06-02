n, s = map(int, input().split())
cur_s = s
refills = 0
for i in range(n):
    order = input()
    try: order = int(order)
    except ValueError: order = int(order[0]) + 1
    if cur_s - order < 0:
        refills += 1
        cur_s = s - order
    else: cur_s -= order
print(refills)