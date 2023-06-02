n = int(input())
if n % 2 == 1:
    print('Invalid')
    exit()
s = input()
stack = ''
for char in s:
    stack+= char
    if len(stack) > 1:
        if stack[len(stack)-2:] == "{}" or stack[len(stack)-2:] == '()' or stack[len(stack)-2:] == '[]':
            stack = stack[0:len(stack)-2]

if len(stack) == 0:
    print('Valid')
else:print('Invalid')