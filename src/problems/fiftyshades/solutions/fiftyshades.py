n = int(input())
s = 0
for i in [0]*n:
    a = input().lower()
    if 'pink' in a:
        s+=1
    elif 'rose' in a:
        s+=1
print(s if s>0 else 'I must watch Star Wars with my daughter')