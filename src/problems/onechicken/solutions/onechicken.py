n, m = map(int, input().split())
l = m - n
if l < 0:
    if -l == 1: print('Dr. Chaz needs 1 more piece of chicken!')
    else: print(f'Dr. Chaz needs {-l} more pieces of chicken!')
else: 
    if l == 1: print('Dr. Chaz will have 1 piece of chicken left over!')
    else: print(f'Dr. Chaz will have {l} pieces of chicken left over!')