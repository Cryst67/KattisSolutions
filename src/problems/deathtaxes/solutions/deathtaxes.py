stocks = 0
average = 0
while True:
    event_deets = input().split()
    event = event_deets[0]
    if event == 'buy':
        x, y = map(float, event_deets[1:])
        average = (stocks * average + x * y)/(stocks+x)
        stocks += x
    if event == 'sell':
        shares, crowns = map(float, event_deets[1:])
        stocks -= shares
    if event == 'split':
        x = float(event_deets[1])
        stocks *= x
        average = average/x
    if event == 'merge':
        x = float(event_deets[1])
        stocks//=x
        average = x*average
    if event =='die':
        x = float(event_deets[1])
        if x - average <= 0:
            print(f'{(stocks * (x))}')
        else:print(stocks * (x - (x - average)*.3))
        break
