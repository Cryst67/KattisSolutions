cups = [1, 0, 0]

test = input()

for i in test:
    if i == "A":
        cups[0], cups[1] = cups[1], cups[0]
    elif i == "B":
        cups[1], cups[2] = cups[2], cups[1]
    elif i == "C":
        cups[0], cups[2] = cups[2], cups[0]

print(cups.index(1) + 1)

