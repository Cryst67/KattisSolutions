score = 0
right = 0
d = {}
while True:
    s = input()
    if s == '-1': break
    time, problem, decision = s.split()
    time = int(time)
    if decision == 'right': 
        right += 1
        if problem in d:
            score += (time + d[problem])
        else: score += time
        continue
    if problem in d: d[problem] +=  + 20
    else: d[problem] = 20

print(right, score)