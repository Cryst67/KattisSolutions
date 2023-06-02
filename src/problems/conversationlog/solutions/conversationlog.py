n = int(input())
d = {}
word_dict = {}
uniques = set()
for _ in range(n):
    line = input().split()
    name, words = line[0], line[1:]
    if name not in d: d[name] = set()
    for word in words:
        d[name].add(word)
        if word not in word_dict:
            word_dict[word] = 1
        else: word_dict[word] += 1
        uniques.add(word)
for word in uniques:
    for name in d:
        if word not in d[name] and word in word_dict:
            word_dict.pop(word)
if len(word_dict) == 0: print("ALL CLEAR")
else:
    final = [k for k, v in sorted(word_dict.items(), key=lambda item: (-item[1], item[0]))]
    for word in final: print(word)
