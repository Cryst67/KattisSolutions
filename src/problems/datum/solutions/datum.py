import datetime
day, month = map(int, input().split())
ans = datetime.date(2009, month, day)
print(ans.strftime("%A"))