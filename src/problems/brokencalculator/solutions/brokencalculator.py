prev = 1
for _ in range(int(input())):
    line = input().split()
    x, y = int(line[0]), int(line[2])
    new = 0
    if line[1] == '+':
        new = (x + y) - prev
    elif line[1] == '-':
        new = prev * (x - y)
    elif line[1] == '*':
        new = (x * y) ** 2
    elif line[1] == '/':
        if x % 2 == 0: new = x//2
        else: new = (x+1)//2
    print(new)
    prev = new