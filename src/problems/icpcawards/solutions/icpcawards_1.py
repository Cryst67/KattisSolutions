d={}
w = []
for i in [0]*int(input()):
 team = input()
 if len(w) ==12:
  continue
 if team.split()[0] not in d:
  w.append(team)
  d[team.split()[0]] = True
print()
for i in w:print(i)