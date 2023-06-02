n = int(input())
for i in range(n):
    r, e, c = map(int, input().split())
    if ((e - c) - r) > 0:
        print('advertise')
    elif ((e - c) - r) == 0:
        print('does not matter')
    else:
        print('do not advertise')