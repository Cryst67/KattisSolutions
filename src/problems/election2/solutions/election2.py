candidates = {}
vote_dist = {}
loop = int(input())
for i in range(loop):
    name = input()
    party = input()
    candidates[name] = party

votes = int(input())
for i in range(votes):
    name = input()
    if name in vote_dist:
        vote_dist[name] += 1
    else:
        vote_dist[name] = 1
winner = ''
max_votes = -10000000000
tie = False
for name in vote_dist:
    if vote_dist[name] > max_votes:
        max_votes = vote_dist[name]
        winner = name
        tie = False
    elif vote_dist[name] == max_votes:
        tie = True

if not tie: print(candidates[winner])
else: print("tie")