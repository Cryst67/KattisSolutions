n = int(input())
beverage = input()

while n > 0:
    if n == 2:
        print(f'2 bottles of {beverage} on the wall, 2 bottles of {beverage}.')
        print(f'Take one down, pass it around, 1 bottle of {beverage} on the wall.')
    elif n == 1:
        print(f'1 bottle of {beverage} on the wall, 1 bottle of {beverage}.')
        print(f'Take it down, pass it around, no more bottles of {beverage}.')
    else:
        print(f'{n} bottles of {beverage} on the wall, {n} bottles of {beverage}.')
        print(f'Take one down, pass it around, {n - 1} bottles of {beverage} on the wall.')
    n -= 1