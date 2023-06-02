def sum_with_sevens(n):
    last_digit = n % 10
    count = 0
    
    if n < 7:
        return -1
    
    if last_digit == 1 and n >= 21:
        count = 3
    elif last_digit == 2 and n >= 42:
        count = 6
    elif last_digit == 3 and n >= 63:
        count = 9
    elif last_digit == 4 and n >= 14:
        count = 2
    elif last_digit == 5 and n >= 35:
        count = 5
    elif last_digit == 6 and n >= 56:
        count = 8
    elif last_digit == 7: count = 1
    elif last_digit == 8 and n >= 28:
        count = 4
    elif last_digit == 9 and n >= 49:
        count = 7
    elif last_digit == 0 and n>= 70:
        count = 10
    if count == 0: return -1
    return count

# Read the input number
for i in range(int(input())):
    print(sum_with_sevens(int(input())))