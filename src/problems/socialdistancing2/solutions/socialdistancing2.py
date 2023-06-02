s, n = map(int, input().split())
seats = [0 for i in range(s)]
l = list(map(int, input().split()))
mini = min(l)
maxi = max(l)
count = 0
for num in l: seats[num - 1] = 1
for i in range(mini - 1, maxi - 2):
    if seats[i] == seats[i + 1] == seats[i + 2]:
        count += 1
        seats[i + 1] = 1
final = [0 for i in range(s - maxi + mini - 1)]
for i in range(len(final) - 2):
    if final[i] == final[i + 1] == final[i + 2]:
        count += 1
        final[i + 1] = 1
print(count)
        
