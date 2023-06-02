n = int(input())
line = []
for i in range(n):
    line.append(input())

events_n = int(input())
events = []
for i in range(events_n):
    events.append(input())

for event in events:
    event_details = event.split()
    op = event_details[0]
    if op == 'cut':
        cutter = event_details[1]
        cuttee = event_details[2]
        line.insert(line.index(cuttee), cutter)
        continue
    line.remove(event_details[1])

for i in range(len(line)):
    print(line[i])