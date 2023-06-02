a, b = input().split()
v = ('a', 'i','o','u')
if a[-1]=='x' and a[-2] == 'e':
    print(f"{a}{b}")
elif a[-1] == 'e':
    print(f"{a}x{b}")
elif v.count(a[-1]) > 0:
    print(f"{a[0:-1]}ex{b}")
else:
    print(f"{a}ex{b}")
    