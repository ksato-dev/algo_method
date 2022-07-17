
n, m = [int(v) for v in input().split()]
a_list = [int(v) for v in input().split()]
b_list = [int(v) for v in input().split()]

# dp[i][j] := i, j の位置における最大ポイント
dp = [[-1] * (m) for _ in range(n)]
dp[0][0] = 0

for i in range(n - 1):
    a = a_list[i]
    b = b_list[i]
    for j in range(m):
        # 今見てる i, j に到達可能でなければスキップ
        if dp[i][j] == -1:
            continue

        # 選ばない時
        dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])

        # 選ぶ時
        if a + j < m:
            dp[i + 1][a + j] = max(dp[i][j] + b, dp[i + 1][a + j])

print(dp[n - 1][m - 1])
