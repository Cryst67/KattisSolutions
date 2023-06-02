n = int(input())
freq = {}
for i in range(n):
    line = input().split()
    category = line[0]
    freq[category] = [set(), 0]
    for key_word in line[2:]:
        freq[category][0].add(key_word)
words = []
while True:
    try: words += input().split()
    except EOFError: break
for word in words:
    for category in freq:
        if word in freq[category][0]: freq[category][1] += 1
maxi = max(list(map(lambda x: x[1], list(freq.values()))))
final = []
for category in freq:
    if freq[category][1] == maxi:
        final.append(category)
final.sort()
for category in final: print(category)