s = input().split()
vowels = ['a', 'e', 'i', 'o', 'u']
for string in s:
    for v in vowels:
        string = string.replace(v+'p' +v, f'{v}')
    print(string, end=' ')