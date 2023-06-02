from math import ceil
s = input()
maxi = float('-inf')
leng = 0
for i in range(len(s)):
    if s[i] == '0':
        leng +=1
    if leng > maxi:
        maxi = leng
    if s[i] == '1':
        leng = 0
print(ceil(maxi/2))