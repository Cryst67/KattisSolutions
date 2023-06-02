n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

ops = [ 
        [0,1,2],
        [0,2,1],
        [1,0,2],
        [1,2,0],
        [2,0,1],
        [2,1,0]
]

best_score = float('-inf')
for op in ops:
    dp_table = [[0 for i in range(n)] for j in range(3)]
    for c in range(n):
        for r in range(3):
            if r == 0 and c == 0:
                if l[c] == op[r]:
                    dp_table[r][c] = 1
            elif r == 0:
                if l[c] == op[r]:
                    dp_table[r][c] = dp_table[r][c-1] + 1
                else:
                    dp_table[r][c] = dp_table[r][c-1]
            elif c == 0:
                if l[c] == op[r]:
                    dp_table[r][c] = 1
                else:
                    dp_table[r][c] = 0
            else:
                if l[c] == op[r]:
                    dp_table[r][c] = max(dp_table[r][c-1] + 1, dp_table[r-1][c-1] + 1)
                else:
                    dp_table[r][c] = max(dp_table[r][c-1], dp_table[r-1][c-1])
    if dp_table[2][n-1] > best_score:
        best_score = dp_table[2][n-1]

print(best_score)