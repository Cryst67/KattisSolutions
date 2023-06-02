s = input()
d = {
    'T' : 0,
    'C' : 0,
    'G' : 0,
}
for letter in s:
    d[letter] += 1
score = 0
mini = float('inf')
for key in d:
    score += d[key] ** 2
    if d[key] < mini:
        mini = d[key]
score += 7 * mini
print(score)