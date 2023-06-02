n = int(input())
transactions = 0
five_hundo = n//500
transactions += five_hundo
n -= five_hundo * 500
two_hundo = n//200
transactions += two_hundo
n -= two_hundo * 200
if n > 0:
    transactions +=1
print(transactions)