dom = {}
kattis = {}
n = int(input())
for i in range(n):
    judge = input()
    if judge in dom: dom[judge] += 1
    else: dom[judge] = 1
    
for i in range(n):
    judge = input()
    if judge in kattis: kattis[judge] += 1
    else: kattis[judge] = 1
    
final = {}
for judgement in dom:
    final[judgement] = min(dom[judgement], kattis.get(judgement, 0))
for judgement in kattis:
    final[judgement] = min(kattis[judgement], dom.get(judgement, 0))
count = 0
for judgement in final: count += final[judgement]
print(count)