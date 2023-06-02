pw1 = input()
pw2 = input()
count = 1
for i in range(4):
    if pw1[i] == pw2[i]:
        count *= 1
    else: count *= 2
print(count)