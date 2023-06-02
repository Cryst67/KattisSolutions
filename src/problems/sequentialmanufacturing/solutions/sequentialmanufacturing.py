n, p = map(int, input().split())
t = list(map(int, input().split()))
input()
print(sum(t) - max(t) + max(t)*p)