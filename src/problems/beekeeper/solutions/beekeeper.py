vowels = 'aeiouy'
while True:
    n = int(input())
    if n == 0: break
    best_word = ''
    double_vowels = float('-inf')
    for i in range(n):
        word = input()
        i = 0
        count = 0
        while i < len(word) - 1:
            if word[i] in vowels:
                if word[i + 1] == word[i]:
                    count += 1
                    i += 2
                    continue
            i += 1
        if count > double_vowels: 
            double_vowels = count
            best_word = word
    print(best_word)