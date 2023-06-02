s = input().split()
d = {s[0][0]: 1}
for i in range(1,len(s)):
    if s[i][0]in d:
        d[s[i][0]] +=1
    else:
        d[s[i][0]] = 1
maxi = 0
for key in d:
    if d[key] > maxi:
        maxi =d[key]
        
print(maxi)
    