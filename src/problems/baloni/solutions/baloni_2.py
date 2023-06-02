n = int(input())
l = map(int, input().split())
buckets = []
mapper = {}
for num in l:
    if num not in mapper:
        buckets.append([num])
        if num == 1: continue
        if num - 1 in mapper: mapper[num - 1].add(len(buckets) - 1)
        else: mapper[num - 1] = set([len(buckets) - 1])
    if num in mapper:
        index = mapper[num].pop()
        if len(mapper[num]) == 0: mapper.pop(num)
        buckets[index].append(num)
        if num != 1:
            if num - 1 in mapper: mapper[num - 1].add(index)
            else: mapper[num - 1] = set([index])
print(len(buckets))