a, b, c = map(int, input().split())
diff_a = b - a - 1
diff_c = c - b - 1
print(max(diff_a, diff_c)) 