a = list(map(int, input().split()))
valid = [1, 2, 3, 4, 5]
while a != valid:
    for i in range(4):
        change = False
        if a[i + 1] < a[i]:
            change = True
            temp = a[i + 1]
            a[i + 1] = a[i]
            a[i] = temp
        if change: 
            for num in a:
                print(num, end= ' ')
            print()