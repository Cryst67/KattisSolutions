words = []
maxi = float('-inf')
while True:
    try: word = input()
    except EOFError: 
        words.sort()
        for w in words:
            for i in range(maxi - len(w)):
                print(' ', end='')
            print(''.join(reversed(w)))
        break
    if word == '': 
        words.sort()
        for w in words:
            for i in range(maxi - len(w)):
                print(' ', end='')
            print(''.join(reversed(w)))
        print()
        words.clear()
        maxi = float('-inf')
        continue
    maxi = max(maxi, len(word))
    words.append(''.join(reversed(word)))