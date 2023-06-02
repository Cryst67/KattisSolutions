while True:
    try:
        a, b = map(int, input().split())
    except EOFError:
        break
    print(abs(a-b))