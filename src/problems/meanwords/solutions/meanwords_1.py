n = int(input())
mean_words = []
max_len = float('-inf')
for i in range(n): 
    word = input()
    max_len = max(len(word), max_len)
    mean_words.append(word)
f = ''
for i in range(max_len):
    sum = 0
    words = 0
    for word in mean_words:
        try: 
            sum += ord(word[i])
            words += 1
        except IndexError: continue
    f += chr(sum//words)
print(f)