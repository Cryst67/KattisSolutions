
while True:
    try: record = input().split()
    except EOFError: break
    heart_rates = []
    name = []
    for i in range(len(record)):
        try: heart_rates.append(float(record[i]))
        except: name.append(record[i])
    print(sum(heart_rates)/len(heart_rates), ' '.join(name))
