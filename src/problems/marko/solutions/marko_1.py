d = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}
n = int(input())
count = 0
words = []
for i in range(n):
    words.append(input())
s = input()
for word in words:
    if len(word) != len(s): continue
    flag = 1
    for i in range(len(s)):
        if word[i] not in d[int(s[i])]:
            flag = 0; break
    if flag: count += 1
print(count)
