words = input().split()
cleaned_words = []
for word in words:
    s = word[0]
    for i in range(1, len(word)):
        if s[-1] == word[i]: continue
        s += word[i]
    cleaned_words.append(s)
print(' '.join(cleaned_words))
        