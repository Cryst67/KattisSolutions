n = int(input())
s = []
prev = ''
for i in range(n):
    s+=["{"+prev+'}']
    prev = f"{','.join(s)}"
print(f"{{{','.join(s)}}}")