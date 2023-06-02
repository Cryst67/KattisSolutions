x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
t = int(input())
manhattan_distance = abs(x1 - x2) + abs(y1 - y2)
if (manhattan_distance % 2 == 0 and t % 2 == 0 and manhattan_distance <= t) or (manhattan_distance % 2 != 0 and t % 2 != 0 and manhattan_distance <= t):
    print('Y')
else: print('N')