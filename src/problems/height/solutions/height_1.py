for i in range(int(input())):
    line = list(map(int, input().split()))
    case, l = line[0], line[1:]
    final = []
    backs = 0
    for i in range(20):
        insertion_index = len(final)
        for j in range(len(final)):
            if final[j] > l[i]:
                insertion_index = j;break
        backs += len(final) - insertion_index
        final.insert(insertion_index, l[i])
    print(case, backs)