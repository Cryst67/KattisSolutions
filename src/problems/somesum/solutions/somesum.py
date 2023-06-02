first = [1]
second = [2]
n = int(input())
i = 1
while i < n:
    first += [first[-1] + 1]
    second += [second[-1] + 1]
    i += 1
s1 = sum(first)
s2 = sum(second)
even = lambda x: x % 2 == 0

if even(s1) and even(s2):
    print('Even')
elif even(s1) and not even(s2) or even(s2) and not even(s1):
    print('Either')
else: print('Odd')