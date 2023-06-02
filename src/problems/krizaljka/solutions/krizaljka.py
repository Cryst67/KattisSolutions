a, b = input().split()
a_index = b_index = -1
for i in range(len(a)):
    try: 
        b_index = b.index(a[i])
        a_index = i
        break
    except ValueError: continue

for i in range(len(b)):
    l = ''
    if i == b_index:
        print(a)
        continue
    for j in range(len(a)):
        if j == a_index:
            l += b[i]
        else: l += '.'
    print(l)