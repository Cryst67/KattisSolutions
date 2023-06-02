cards = []
flipped = []

def cascade(flipped):
    if len(flipped) < 3:
        return flipped
    rmv = 1
    while rmv:
        rmv = 0
        rank = 0
        suit = 0
        for i in range(len(flipped) - 1, 2, -1):
            c1 = flipped[i]
            c2 = flipped[i - 3]
            if not rank and c1[0] == c2[0]:
                rank = i
            if not suit and c1[1] == c2[1]:
                suit = i
        if rank: flipped = flipped[:rank - 3] + flipped[rank+ 1:]; rmv = 1
        elif suit: flipped = flipped[:suit - 3] + flipped[suit - 2: suit] + flipped[suit + 1:]; rmv = 1
    return flipped

for i in range(4): cards += input().split()
for card in cards: 
    flipped.append(card)
    flipped = cascade(flipped)
print(len(flipped), ' '.join(flipped))