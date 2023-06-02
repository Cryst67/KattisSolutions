for i in range(int(input())):
    r, p, d = map(int, input().split())
    scaling_factor = d/p
    scaled_weight = -1
    d = {}
    for _ in range(r):
        line = input().split()
        name = line[0]
        w, per = map(float, line[1:])
        d[name] = (w, per)
        if per == 100.0:
            scaled_weight = w * scaling_factor
    print(f'Recipe # {i + 1}')
    for key in d:
        print(f'{key} {(d[key][1] * .01 * scaled_weight):.1f}')
    print(''.join(['-' for i in range(40)]))