n = input()
def get_sum(n):
    s = 0
    for dig in n:
        s+=int(dig)
    return s
s = get_sum(n)
while int(n)%s != 0:
    n = int(n)+1
    n = str(n)
    s = get_sum(n)
print(n)
