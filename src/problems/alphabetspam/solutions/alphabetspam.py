s = input()
upper = 0
lower = 0
underline = 0
other = 0
for letter in s:
    if letter.isupper():
        upper += 1
    elif letter.islower():
        lower += 1
    elif letter == '_':
        underline += 1
    else:
        other += 1

print(underline/len(s))
print(lower/len(s))
print(upper/len(s))
print(other/len(s))