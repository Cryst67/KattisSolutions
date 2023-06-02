KEY = 'welcome to code jam'


def parse(key, string, index=0):
    if index >= len(key):
        return 1
    count = 0
    for i in range(len(string)):
        if string[i] == key[index]:
            count += parse(key, string[i+1:len(string)], index+1)

    return count


def generate_zeros(n):
    s = ''
    for _ in range(n):
        s += '0'
    return s


def get_last_four(s):
    s = str(s)
    return s[-4:len(s)]


n = int(input())
tests = []
for _ in range(n):
    test_case = input()
    tests.append(test_case)

for i in range(len(tests)):
    test = tests[i]
    out = parse(key=KEY, string=test)
    if out >= 1000:
        out = get_last_four(out)
    else:
        digits = len(str(out))
        s = generate_zeros(4 - digits)
        out = s + str(out)
    print(f"Case #{i + 1}: {out}")
