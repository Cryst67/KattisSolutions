n = input()
while True:
    prod = 1
    for i in n:
        if i == '0': continue
        prod *= int(i)
    if prod < 10:
        print(prod)
        break
    n = str(prod)