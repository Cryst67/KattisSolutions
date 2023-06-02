def get_divisors(n):
    l = []
    for i in range(1, int(n **.5) + 1):
        if n % i == 0:
            l.append(i)
    divisors = set()
    for num in l:
        divisors.add(num)
        divisors.add(n // num)
    return sorted(list(divisors))

n = int(input())
divisors = get_divisors(n)
i = 1
count = 1
while n != 1:
    if n % divisors[i] == 0: n//=divisors[i];count += 1
    else: i += 1
print(count)