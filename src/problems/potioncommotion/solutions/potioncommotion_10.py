N, M, P = map(int, input().split())
attacks = list(map(int, input().split()))
health = N
potions = P

if max(attacks) >= N:
    print('next time')
    exit()
all_damages = sum(attacks)
if all_damages >= N + (P * 20):
    print('next time')
    exit()

for i in range(M):
    health -= attacks[i]
    if health <= 0:
        print('next time')
        break
    if i + 1 == M:
        print('champion')
        break
    if health > attacks[i + 1]:
        continue
    if health <= attacks[i + 1]:
        while health <= attacks[i + 1] and potions != 0:
            potions -= 1
            health += 20
            if health > N:
                health = N
    if health - attacks[i + 1] <= 0:
        print('next time')
        break
