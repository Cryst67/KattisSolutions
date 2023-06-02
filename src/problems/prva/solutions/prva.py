r, c = map(int, input().split())
words = []
top_down_words = ['' for i in range(c)]
for i in range(r):
    w = input()
    words.append(w)
    for i in range(len(w)):
        top_down_words[i] += w[i]
satisfying = []
for word in words:
    if '#' in word:
        l = word.split('#')
        for word2 in l:
            if len(word2) > 1: satisfying.append(word2)
    else: satisfying.append(word)
for word in top_down_words:
    if '#' in word:
        l = word.split('#')
        for word2 in l:
            if len(word2) > 1: satisfying.append(word2)
    else: satisfying.append(word)
print(sorted(satisfying)[0])