found = 0
for _ in range(int(input())):
    n = int(input())
    name = input()
    pea = pan = 0
    for i in range(n):
        item = input()
        if item == 'pea soup':
            pea = 1
        elif item == 'pancakes':
            pan = 1
    if pea and pan:
        print(name)
        found = 1
        break
if not found:
    print('Anywhere is fine I guess')
        