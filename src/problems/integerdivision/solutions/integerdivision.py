n, d = map(int, input().split())
l = list(map(int, input().split()))
int_div_d = {}
for num in l:
    int_div = num//d
    if int_div not in int_div_d:
        int_div_d[int_div] = 1
        continue
    int_div_d[int_div] += 1
c = 0
for key in int_div_d:
    num = int_div_d[key]
    c += ((num - 1)*(num))//2
print(c)