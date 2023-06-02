while True:
    try: s = input()
    except EOFError: break
    stack = [s[0]]
    f = ''
    for i in range(1, len(s)):
        if s[i] == stack[-1]:
            stack.append(s[i])
        else:
            f += f'{len(stack)}{stack[-1]}'
            stack.clear()
            stack.append(s[i])
    if len(stack) != 0:
        f += f'{len(stack)}{stack[-1]}'
    print(f)