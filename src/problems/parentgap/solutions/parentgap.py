def sunday(year, month, n):
    first = calendar.monthrange(year, month)[0]
    if first == 6:
        first = 1
    else: first = 7 - first
    return first + 7*(n - 1)
import calendar
year = int(input())
print(abs(31 - sunday(year, 5, 2) + sunday(year, 6, 3))//7, 'weeks')