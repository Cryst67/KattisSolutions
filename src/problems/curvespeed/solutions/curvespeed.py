while True:
    try: r, s = map(float, input().split())
    except EOFError: break
    print(round(((r * (s + 0.16))/0.067)**0.5))