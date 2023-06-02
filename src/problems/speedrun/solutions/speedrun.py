class Task:
    def __init__(self, start, end):
        self.start = start
        self.end = end

g, n = map(int, input().split())
tasks = []
for i in range(n):
    ts, te = map(int, input().split())
    tasks.append(Task(ts, te))

tasks.sort(key = lambda x: x.end)
cur_time = tasks[0].end
completed = 1
for i in range(1, n):
    if tasks[i].start >= cur_time:
        completed += 1
        cur_time = tasks[i].end
print('YES' if completed >= g else 'NO')