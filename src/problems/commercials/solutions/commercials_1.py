def max_function(sequence, p):
    max_value = float('-inf')
    current_sum = 0
    window_start = 0

    for window_end, number in enumerate(sequence):
        current_sum += number

        while current_sum - p * (window_end - window_start + 1) < 0:
            current_sum -= sequence[window_start]
            window_start += 1

        max_value = max(max_value, current_sum - p * (window_end - window_start + 1))

    return max_value
n, p = map(int, input().split())
l = [*map(int, input().split())]
print(max_function(l, p))
        