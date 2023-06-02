while True:
    try: case = input().replace(' ', '')
    except EOFError: break
    print(f'{eval(case):.2f}')