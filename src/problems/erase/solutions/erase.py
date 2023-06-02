n = int(input())
first = input()
second = input()
if n % 2 == 0:
    if first == second: print('Deletion succeeded')
    else: print('Deletion failed')
    exit()
first = list(first)
for i in range(len(first)):
    if first[i] == '0': first[i] = '1'
    else: first[i] = '0'
first = ''.join(first)
if first == second: print('Deletion succeeded')
else: print('Deletion failed')