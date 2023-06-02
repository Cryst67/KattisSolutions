class Name:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
names = []
first_names = {}
while True:
    try: first, last = input().split()
    except EOFError: break
    names += [Name(first, last)]
    if first in first_names:
        first_names[first] += 1
    else: first_names[first] = 1
names.sort(key=lambda x: (x.last, x.first))
for name in names:
    if first_names[name.first] > 1:
        print(name.first, name.last)
    else: print(name.first)
    
    