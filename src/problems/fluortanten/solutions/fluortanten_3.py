n = int(input())
queue = list(map(int, input().split()))

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


if n < 1001:
    zero = queue.index(0)
    max = get_sum(queue)
    for i in range(n):
        if i != zero:
            q = move_zero(queue, i)
            if get_sum(q) > max:
                max = get_sum(q)
    print(max)
    exit()

zero_index = queue.index(0) + 1

m_h_index = 0
l_h_index = 0

most_happiness = queue[0] * (m_h_index + 1)
least_happiness = queue[0] * (l_h_index + 1)

for i in range(1, n):
    if queue[i] * (i + 1) > most_happiness:
        most_happiness = queue[i] * (i + 1)
        m_h_index = i
    if queue[i] * (i + 1) < least_happiness:
        least_happiness = queue[i] * (i + 1)
        l_h_index = i

if m_h_index > zero_index and l_h_index < zero_index:
    print(sum(queue))
    exit()

new_a = move_zero(queue, m_h_index)
new_a2 = move_zero(queue, l_h_index)
print(max(get_sum(new_a), get_sum(new_a2)))
