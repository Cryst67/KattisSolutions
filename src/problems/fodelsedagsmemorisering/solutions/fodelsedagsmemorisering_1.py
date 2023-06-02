d = {}
for _ in range(int(input())):
    name, like, dob = input().split()
    if dob not in d:
        d[dob] = (name, like)
    else:
        if int(like) > int(d[dob][1]):
            d[dob] = (name, like)
a = []
for i in d:
    a.append(d[i][0])
a.sort()
print(len(a))
for i in a:
    print(i) 