p, d = map(int, input().split())
di = {i: {'total' : 0, 'A': 0, 'B': 0} for i in range(1, d+1)}
sum_total = 0
for i in range(p):
    district, a, b = map(int, input().split())
    di[district]['A'] += a
    di[district]['B'] += b
    di[district]['total'] += (a + b)
    sum_total += (a+b)
wasted_a = 0
wasted_b = 0
for key in di:
    solution = ''
    cur = di[key]
    if cur['A'] > cur['B']: 
        solution += 'A '
        solution += str(cur['A'] - (cur['total']//2 + 1))
        wasted_a += (cur['A'] - (cur['total']//2 + 1))
        solution += ' '
        solution += str(cur['B'])
        wasted_b += cur['B']
    else: 
        solution += 'B '
        solution += str(cur['A'])
        wasted_a += cur['A']
        solution += ' '
        solution += str(cur['B'] - (cur['total']//2 + 1))
        wasted_b += (cur['B'] - (cur['total']//2 + 1))
    print(solution)
print(abs(wasted_a - wasted_b)/sum_total)