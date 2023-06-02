n = input()
indices = []
for i in range(len(n) - 1):
    if n[i] == ':' or n[i] == ';':
        if n[i + 1] == '-':
            if i == len(n) - 2:
                continue
            if n[i + 2] == ')':
                indices.append(i)
                continue
        if n[i + 1] == ')':
            indices.append(i)
            
for num in indices:
    print(num)