from functools import reduce
vic_cards_key = ['Province', 'Duchy', 'Estate']
vic_cards = [8,5,2]
tr_cards_key = ['Gold', 'Silver', 'Copper']
tr_cards = [
        {
        'tr' : 'Gold',
        'cost' : 6,
        'val': 3
        },
        {
        'tr' : 'Silver',
        'cost': 3,
        'val': 2,
        },
        {
        'tr': 'Copper',
        'cost':0,
        'val':1,
        },
]

test_case = list(input().split(' '))
user_cards = list(map(lambda x : int(x), test_case))
buying_powers = [tr_cards[i]['val']*x for i, x in enumerate(user_cards)]
total_power = reduce(lambda x, y: x + y, buying_powers, 0)
best_vic = list(filter(lambda x: x - total_power <= 0, vic_cards))
best_tr = list(filter(lambda x: x['cost'] - total_power <= 0, tr_cards))
final = []
if len(best_vic) > 0:
    final.append(vic_cards_key[vic_cards.index(max(best_vic))])
if len(best_tr) > 0:
    final.append(best_tr[0]['tr']) 

if len(final) == 1:
    print(final[0])
else: print(f"{final[0]} or {final[1]}")