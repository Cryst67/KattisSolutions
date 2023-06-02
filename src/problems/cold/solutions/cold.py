n = input()
l = list(map(int, input().split()))
neg = list(filter(lambda x: x < 0, l))
print(len(neg))