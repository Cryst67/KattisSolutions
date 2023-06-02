n = int(input())
a = list(map(int, input().split()))

zero_index = a.index(0) + 1

m_h_index = 0
l_h_index = 0

most_happiness = a[0] * (m_h_index + 1)
least_happiness = a[0] * (l_h_index + 1)

def move_zero(queue, i): 
    q = queue.copy()
    q.remove(0)
    q.insert(i, 0)
    return q

def get_sum(queue):
    sum = 0
    for i in range(n):
        sum += queue[i] * (i + 1)
    return sum

for i in range(1, n):
    if a[i] * (i + 1) > most_happiness:
        most_happiness = a[i] * (i + 1)
        m_h_index = i
    if a[i] * (i + 1) < least_happiness:
        least_happiness = a[i] * (i + 1)
        l_h_index = i

if m_h_index > zero_index and l_h_index < zero_index:
    print(sum(a))
    exit()

new_a = move_zero(a, m_h_index)
new_a2 = move_zero(a, l_h_index)
print(max(get_sum(new_a), get_sum(new_a2)))