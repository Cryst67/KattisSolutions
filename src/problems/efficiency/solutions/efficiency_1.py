p, m = int(input()), int(input())
words = ['Efficiency', 'Unbreaking', 'Silk', 'Touch']
rounds = 1
turns = 0
prev = 0
while turns < m:
    turns_this_round = rounds * 4
    for i in range(1, turns_this_round + 1):
        cur = i + turns
        if cur == m:
            if i <= rounds:
                print(words[0])
            elif i <= rounds*2:
                print(words[1])
            else:
                if i % 2 != 0:
                    print(words[2])
                else: print(words[3])
    turns += prev + 4
    prev += 4
    rounds += 1
if p > turns:
    print(turns)
else:
    if turns % p == 0:
        print(p)
    else: print(turns % p)
