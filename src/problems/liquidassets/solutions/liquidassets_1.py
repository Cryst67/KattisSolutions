input()
words = input().split()
new_words = []
vowels = ['a', 'e', 'i', 'o', 'u']
for word in words:
    i = 0
    new_word = ''
    while i < len(word):
        if i == len(word) - 1:
            new_word += word[i]
            i += 1
        elif word[i] == word[i + 1]:
            while i < len(word) - 1 and word[i] == word[i + 1]:
                i += 1
            new_word += word[i]
            i += 1
        else: 
            new_word += word[i]
            i += 1
    final = ''
    for j in range(len(new_word)):
        if j == 0 or j == len(new_word) - 1: final += new_word[j]
        else:
            if new_word[j] in vowels: continue
            final += new_word[j]
    new_words.append(final)
print(' '.join(new_words))