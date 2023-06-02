cards = {}
suits = {'P':0,
         'K':0,
         'H':0,
         'T':0
}
s = input()
i = 0
while i < len(s):
    card = s[i:i+3]
    if card in cards:
        print("GRESKA")
        exit()
    cards[card] = 1
    suits[card[0]] += 1
    i+= 3

for key in suits:
    print(13 - suits[key], end=' ')
print()
