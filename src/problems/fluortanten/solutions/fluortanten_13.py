n = int(input())
queue = list(map(int, input().split(' ')))

def get_sum(queue):
    sum = 0
    for i in range(n):
        sum += queue[i] * (i + 1)
    return sum

def move_zero(queue):
    queue.remove(0)
    queue.append(0)
    return queue

queue = move_zero(queue)
max = get_sum(queue)
print(queue)
print(max)