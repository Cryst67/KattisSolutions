test_case = input().split(' ')
[e, f, c] = [int(x) for x in test_case]
bottles = e + f
consumed = 0
while True:
    if bottles - c >= 0:
        bottles -= c
        bottles += 1
        consumed += 1
    else:
        break

print(consumed)
    