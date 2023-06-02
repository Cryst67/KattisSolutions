frequency = [0 for i in range(1001)]
d = {}
s = input()
for letter in s:
    if letter in d:
        d[letter] += 1
    else: d[letter] = 1
max_odd = 0
for key in d:
    frequency[d[key]] += 1
    if d[key] % 2 != 0:
        max_odd = max(max_odd, d[key])

un_needed = 0
for i in range(1, 1001):
    if frequency[i] != 0:
        if i % 2 == 1:
            if i == max_odd:
                un_needed += frequency[i] - 1
            else:
                un_needed += frequency[i]
print(un_needed)