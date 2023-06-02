def generate_strings(n):
    if n == 0:
        return ['']
    else:
        prev_strings = generate_strings(n-1)
        new_strings = []
        for s in prev_strings:
            new_strings.append(s+'2')
            new_strings.append(s+'4')
        return new_strings

n = input()
l = len(n)
a = []
n = int(n)
while l >= 1:
    a.append(generate_strings(l))
    l-=1
ans = []
for i in range(len(a)):
    for j in range(len(a[i]) - 1, -1, -1):
        num = int(a[i][j])
        if n % num == 0:
            ans.append(num)
for i in range(len(ans) - 1, -1, -1):
    print(ans[i])