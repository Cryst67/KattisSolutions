top_bottom = 0
left_right = 0
for _ in range(int(input())):
    s = input()
    for i in range(2):
        if s[i] == '0': top_bottom += 1
    for i in range(2, 4):
        if s[i] == '0': left_right += 1

print(min(top_bottom, left_right)//2, top_bottom - (min(top_bottom, left_right)//2) * 2, left_right - (min(top_bottom, left_right)//2)* 2)
