for i in range(int(input())):
    input()
    d = {}
    l = input().split()
    red = []
    blue = []
    for t in l:
        length = int(t[:-1])
        color = t[-1]
        if color == 'R': red.append(length)
        else: blue.append(length)
    red = sorted(red, reverse=1)
    blue = sorted(blue, reverse=1)
    mini = min(len(red), len(blue))
    red = red[:mini]
    blue = blue[:mini]
    print(f"Case #{i+1}: {max(0, sum([sum(red), sum(blue)]) - 2*(len(red)))}")