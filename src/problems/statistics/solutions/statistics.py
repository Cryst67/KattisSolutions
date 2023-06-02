case = 1
while True:
    try: s = input()
    except EOFError: break
    nums = [*map(int, s.split())][1:]
    maxi = max(nums)
    mini = min(nums)
    print(f"Case {case}: {mini} {maxi} {maxi - mini}")
    case += 1