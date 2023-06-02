for _ in range(int(input())):
    n, m = map(int, input().split())
    prizes = []
    winnings = 0
    for _ in range(n):
        line = list(map(int, input().split()))
        stickers = line[1:-1]
        cash = line[-1]
        if cash > 0: prizes.append((cash, (stickers)))
    sticker_inventory = list(map(int, input().split()))
    prizes.sort(key = lambda x: x[0])
    for prize in prizes:
        req_stickers = prize[1]
        cash = prize[0]
        cap = float('inf')
        for sticker in req_stickers:
            cap = min(cap, sticker_inventory[sticker - 1])
        winnings += cap * cash
        for sticker in req_stickers:
            sticker_inventory[sticker - 1] -= cap
    print(winnings)