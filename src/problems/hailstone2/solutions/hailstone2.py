n = int(input())
sequence = [n]
count = 0
while True:
    cur = sequence[count]
    if cur == 1: break
    if cur % 2 == 0:
        sequence.append(cur/2)
        count += 1
        continue
    sequence.append((3*cur) + 1)
    count += 1

print(count + 1)