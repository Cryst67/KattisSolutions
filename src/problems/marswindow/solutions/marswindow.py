month = 4
check_year = int(input())
year = 2018
while year < check_year:
    month +=2
    year +=2
    if month - 12 > 0:
        month -=12
        year+=1
if year==check_year:
    print('yes')
    exit()
print('no')
