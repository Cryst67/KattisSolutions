def mapper_pop(mapper, num):
    index = mapper[num].pop()
    if len(mapper[num]) == 0: mapper.pop(num)
    return index

def mapper_add(mapper, num, index):
    if num == 1: return
    if num - 1 in mapper: mapper[num - 1].add(index)
    else: mapper[num - 1] = set([index])

def main():
    n = int(input())
    l = map(int, input().split())
    buckets = []
    mapper = {}
    for num in l:
        if num not in mapper:
            buckets.append([num])
            mapper_add(mapper, num, len(buckets) - 1)
        if num in mapper:
            index = mapper_pop(mapper, num)
            buckets[index].append(num)
            mapper_add(mapper, num, index)
    print(len(buckets))
        
if __name__ == '__main__':
    main()