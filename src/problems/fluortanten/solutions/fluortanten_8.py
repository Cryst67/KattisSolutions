n = int(input())
a = list(map(int, input().split()))
least_happy = a[0] * 1
least_happy_index = 1
most_happy = a[0] * 1
most_happy_index = 1
zero_index = a.index(0) + 1
happiness_score = 0
for i in range(1, n):
    if a[i] * (i + 1) < least_happy:
        least_happy = a[i] * (i + 1)
        least_happy_index = i + 1
    if a[i] * (i + 1) > most_happy:
        most_happy = a[i] * (i + 1)
        most_happy_index = i + 1
    happiness_score += a[i] * (i + 1)


if least_happy_index < zero_index and most_happy_index < zero_index:
    a.remove(0)
    a.insert(most_happy_index - 1, 0)
    happiness_score = 0
    for i in range(n):
        happiness_score += a[i] * (i + 1)
    print(happiness_score)
    exit()

new_a = a.copy()

if least_happy_index > zero_index:
    a.remove(0)
    a.insert(least_happy_index - 1, 0)

    happiness_score = 0
    for i in range(n):
        happiness_score += a[i] * (i + 1)
    print(happiness_score)