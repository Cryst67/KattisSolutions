n = int(input())
queue = list(map(int, input().split(' ')))

def get_sum(queue):
    sum = 0
    for i in range(n):
        sum += queue[i] * (i + 1)
    return sum
zero = queue.index(0)
max = get_sum(queue)

def move_zero(queue, i):
    queue.remove(0)
    queue.insert(i, 0)
    return queue

for i in range(n):
    if i != zero:
        q = move_zero(queue, i)
        new_sum = get_sum(q)
        if new_sum > max:
            max = new_sum
print(max)