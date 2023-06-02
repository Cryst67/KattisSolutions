alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(int(input())):
    d = {alphabet[i]: 0 for i in range(26)}
    s = input()
    for letter in s:
        letter = letter.lower()
        if letter in d: d[letter] = 1
    missing = ''
    for key in d:
        if d[key] == 0: missing += key
    print('pangram' if missing == '' else f'missing {missing}')