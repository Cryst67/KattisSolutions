def find_biggest_peak(l):
    n = len(l)
    max_peak = 0

    for i in range(1, n - 1):
        if l[i - 1] <= l[i] >= l[i + 1]:
            left_min, right_min = l[i - 1], l[i + 1]
            j, k = i - 1, i + 1

            while j > 0 and l[j - 1] <= l[j]:
                j -= 1
                left_min = min(left_min, l[j])

            while k < n - 1 and l[k + 1] <= l[k]:
                k += 1
                right_min = min(right_min, l[k])

            peak = min(l[i] - left_min, l[i] - right_min)
            max_peak = max(max_peak, peak)

    return max_peak

def remove_consecutive_duplicates(l):
    unique_list = [l[0]]
    for i in range(1, len(l)):
        if l[i] != l[i - 1]:
            unique_list.append(l[i])
    return unique_list

n = int(input())
l = remove_consecutive_duplicates(list(map(int, input().split())))
print(find_biggest_peak(l))
