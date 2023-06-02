s = set()
n, k = map(int, input().split())
class Pokenom:
    def __init__(self, i, attack, defense, health) -> None:
        self.id = i
        self.attack = attack
        self.defense = defense
        self.health = health
l = []
for i in range(n):
    a, b, c = map(int, input().split())
    l += [Pokenom(i, a, b, c)]
l.sort(key = lambda x: x.attack, reverse=1)
for i in range(k): s.add(l[i].id)
l.sort(key = lambda x: x.defense, reverse=1)
for i in range(k): s.add(l[i].id)
l.sort(key = lambda x: x.health, reverse=1)
for i in range(k): s.add(l[i].id)
print(len(s))