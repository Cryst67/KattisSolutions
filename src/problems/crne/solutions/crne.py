n = int(input())
temp = (n//2)+1
ans = temp**2
if n % 2 == 1:
    ans += temp
print(ans)