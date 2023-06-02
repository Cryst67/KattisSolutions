d = {}
students = set()
project = ''
while True:
    line = input()
    if line == '1':
        keys = sorted(list(d.keys()), key=lambda x: (-len(d[x]), x))
        for key in keys:
            print(key, len(d[key]))
        d.clear(); students.clear()
        continue
    if line == '0':
        break
    if line.isupper():
        project = line
        d[project] = set()
        continue
    if line in students:
        flag = 0
        for proj in d:
            if line in d[proj] and proj != project: 
                d[proj].remove(line)
                flag = 1
        if flag:
            if line in d[project]:
                d[project].remove(line)
        continue
    students.add(line)
    d[project].add(line)

