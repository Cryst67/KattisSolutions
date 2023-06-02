for j in range(int(input())):
    s1, s2 = input(), input()
    oop_fm = {'0': 0, '1': 0}
    unsure_fm = {'0':0, '1': 0}
    for i in range(len(s1)):
        if s1[i] == '?':
            unsure_fm[s2[i]] += 1
            continue
        if s1[i] != s2[i]: oop_fm[s1[i]] += 1
    moves = 0
    swaps = min(oop_fm['0'], oop_fm['1'])
    for key in oop_fm: oop_fm[key] -= swaps
    unsure_zero_swaps = min(oop_fm['0'], unsure_fm['0'])
    unsure_fm['0'] -= unsure_zero_swaps
    oop_fm['0'] -= unsure_zero_swaps
    unsure_one_swaps = min(oop_fm['1'], unsure_fm['1'])
    unsure_fm['1'] -= unsure_one_swaps
    oop_fm['1'] -= unsure_one_swaps
    moves += unsure_one_swaps * 2
    moves += unsure_zero_swaps * 2
    moves += unsure_fm['0']
    moves += unsure_fm['1']
    moves += swaps
    moves += oop_fm['0']
    if oop_fm['1'] > 0:
        print(f'Case {j + 1}: -1')
        continue
    print(f'Case {j + 1}: {moves}')