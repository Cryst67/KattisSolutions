stack = []
s = input()
for char in s:
    if len(stack) == 0 and char == '<':
        continue
    if char == '<':
        stack.pop()
    else: stack.append(char)
print(''.join(stack))