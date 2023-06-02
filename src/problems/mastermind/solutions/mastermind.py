line = input().split()
n = int(line[0])
code, guess = line[1:]
r = s = 0
code_map = {}
guess_map = {}
for i in range(n):
    if code[i] == guess[i]: r += 1; continue
    if code[i] in code_map: code_map[code[i]] += 1
    else: code_map[code[i]] = 1
    if guess[i] in guess_map: guess_map[guess[i]] += 1
    else: guess_map[guess[i]] = 1
for letter in guess_map:
    s += min(guess_map[letter], code_map.get(letter, 0))
        
print(r, s)