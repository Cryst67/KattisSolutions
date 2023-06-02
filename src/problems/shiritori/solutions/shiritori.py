n = int(input())
s = set()
first = input()
s.add(first)
prev = first[-1]
prev_len = 1
turn = 2
for i in range(n - 1):
    word = input()
    s.add(word)
    if word[0] != prev or len(s) == prev_len:
        print(f'Player {turn} lost')
        exit()
    prev = word[-1]
    prev_len = len(s)
    if turn == 2: turn = 1
    else: turn = 2


print('Fair Game')