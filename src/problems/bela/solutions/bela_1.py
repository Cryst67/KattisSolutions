domHand = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'J': 20,
    'T': 10,
    '9': 14,
    '8': 0,
    '7': 0,
}

nonDomHand = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'J': 2,
    'T': 10,
    '9': 0,
    '8': 0,
    '7': 0,
}

hands, domSuit = input().split(' ')
hands = int(hands)
sum = 0
for _ in range(hands*4):
    card = input()
    if card[1] == domSuit:
        sum += domHand[card[0]]
    else:
        sum += nonDomHand[card[0]]

print(sum)
