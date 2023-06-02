from typing import List
cards = []
flipped = []

def check(c1, c2):
    if c1[0] == c2[0]: return 4
    if c1[1] == c2[1]: return 2
    return 0

def cascade(flipped: List):
    if len(flipped) < 3:
        return flipped
    removed = True
    while removed:
        removed = False
        first_rank_match = None
        first_suit_match = None
        for i in range(len(flipped) - 1, 2, -1):
            if first_rank_match is None and flipped[i][0] == flipped[i-3][0]:
                first_rank_match = i
            if first_suit_match is None and flipped[i][1] == flipped[i-3][1]:
                first_suit_match = i
        if first_rank_match is not None:
            flipped = flipped[:first_rank_match - 3] + flipped[first_rank_match + 1:]
            removed = True
        elif first_suit_match is not None:
            flipped = flipped[:first_suit_match - 3] + flipped[first_suit_match - 2:first_suit_match] + flipped[first_suit_match + 1:]
            removed = True
    return flipped

for i in range(4): cards += input().split()
for card in cards: 
    flipped.append(card)
    flipped = cascade(flipped)
print(f"{len(flipped)} {' '.join(flipped)}")