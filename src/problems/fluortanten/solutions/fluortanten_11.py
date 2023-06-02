n = int(input())
queue = list(map(int, input().split(' ')))

def get_sum(queue):
    sum = 0
    for i in range(n):
        sum += queue[i] * (i + 1)
    return sum

def move_zero(queue, i):
    queue.remove(0)
    queue.insert(i, 0)
    return queue

def find_smallest(queue):
    ind = 0
    smallest = queue[0] * (ind + 1)
    for i in range(1, n):
        if queue[i] * (i + 1) < smallest:
            smallest = queue[i] * (i + 1)
            ind = i
    return ind

def find_largest(queue):
    ind = 0
    largest = queue[0] * (ind + 1)
    for i in range(1, n):
        if queue[i] * (i + 1) > largest:
            largest = queue[i] * (i + 1)
            ind = i
    return ind

smallest_ind = find_smallest(queue)
largest_ind = find_largest(queue)
zero_ind = queue.index(0)
q = []
if zero_ind < smallest_ind:
    q = move_zero(queue, smallest_ind)
else:
    q = move_zero(queue, largest_ind)

print(q, get_sum(q))