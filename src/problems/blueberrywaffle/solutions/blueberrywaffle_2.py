a, b = map(int, input().split())
ans = ''
if int(b/a) % 2 == 0 and b % a < int(a/2):
    ans = 'up'
elif int(b/a) % 2 == 1 and b % a > int(a/2):
    ans = 'up'
else: 
    ans = 'down'
print(ans)