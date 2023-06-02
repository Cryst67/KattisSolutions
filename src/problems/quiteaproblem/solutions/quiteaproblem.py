while True:
    try:
        s = input()
    except EOFError:
        break
    if 'problem' in s.lower():
        print('yes')
    else:
        print('no')