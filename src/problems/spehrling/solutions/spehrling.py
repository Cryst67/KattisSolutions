word = input()
correct_word = input()
first_wrong = -1
for i in range(min(len(word), len(correct_word))):
    if word[i] != correct_word[i]: first_wrong = i; break
if first_wrong == -1: print(abs(len(word) - len(correct_word)))
else: 
    f = 0
    f += len(word) - first_wrong
    f += len(correct_word) - first_wrong
    print(f)