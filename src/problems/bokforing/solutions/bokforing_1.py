n, q = map(int, input().split())
d = {i + 1: 0 for i in range(n)}
changed = {}
cur_changed = 0
def set_value(i, x):
    d[i] = x
    changed[i] = True

def restart(changed, x):
    changed = {}
    cur_changed = x
    return changed, cur_changed


def print_value(i, cur_changed):
    if i in changed:
        print(d[i])
    else:
        print(cur_changed)

for _ in range(q):
    task = input().split()
    if len(task) == 3:
        i, x = map(int, task[1:])
        set_value(i, x)
    else:
        if task[0] == 'PRINT':
            i = int(task[1])
            print_value(i, cur_changed)
        else:
            x = int(task[1])
            changed, cur_changed = restart(changed, x)
