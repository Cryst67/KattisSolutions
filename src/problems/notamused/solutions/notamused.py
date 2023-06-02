import sys
log = {}
entered = {}
def print_report(day, log):
    names = sorted(list(log.keys()))
    print(f'Day {day}')
    for name in names:
        print(name, f'${log[name]:.2f}')

lines = sys.stdin.readlines()
day = 0
for i in range(len(lines)):
    line = lines[i].split()
    if line[0] == 'OPEN': log.clear(); entered.clear(); continue
    elif line[0] == 'CLOSE':
        day += 1
        if i == len(lines) - 1: print_report(day, log)
        else: print_report(day, log);print()
    elif line[0] == 'ENTER':
        person = line[1]
        time = int(line[2])
        entered[person] = time
    elif line[0] == 'EXIT':
        person = line[1]
        time = int(line[2])
        cost = (time - entered[person]) * 0.1
        entered.pop(person)
        if person in log: log[person] += cost
        else: log[person] = cost