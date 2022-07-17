
n, m = [int(v) for v in input().split()]
a_list = [int(v) for v in input().split()]

# dp[i][j] := i, j 要素にたどりつけるかどうか
dp = [[False] * m for _ in range(n)]
dp[0][0] = True

for i in range(n - 1):
    for j in range(m):
        if not dp[i][j]:
            continue

        dp[i + 1][j] = True

        next_j = a_list[i] + j
        if next_j < m:
            dp[i + 1][next_j] = True

print(sum(dp[n - 1]))
