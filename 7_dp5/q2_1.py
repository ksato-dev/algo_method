
n = 4
table = [[0] * n for _ in range(n)]
table[0] = [int(v) for v in input().split()]

for i in range(1, n):
    for j in range(n):
        curr_sum = 0
        if 0 <= j - 1:
            curr_sum += table[i - 1][j - 1]
        if j + 1 < n:
            curr_sum += table[i - 1][j + 1]
        curr_sum += table[i - 1][j]
        table[i][j] = curr_sum

print(table[n - 1][n - 1])
