n = int(input())
money = 0
od_protect = 0
for i in range(n):
    num = int(input())
    if num > 0: money += num
    if num < 0:
        if money + num < 0:
            od_protect += abs(money + num)
            money += abs(money+num)
        money += num
print(od_protect)