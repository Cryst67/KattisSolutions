def recur(i, n):
    a = str(len(n))
    if a == n: return i
    return recur(i+1, str(a))
while True:
    n = input()
    if n == 'END': break
    print(recur(1, n))