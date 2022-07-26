
n, m = [int(v) for v in input().split()]
w_list = [int(v) for v in input().split()]

# dp[i][j] := i 個のボール（0~i-1）を使って、重さ j にするための最小のボール数
inf = 10 ** 10
dp = [[inf] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    w = w_list[i]
    for j in range(m + 1):
        # i, j のときの状態が存在しない場合は次の問題を解けないので飛ばす。
        if dp[i][j] == inf:
            continue

        # 選ばない時
        dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])

        # 選ぶ時
        if j + w <= m:
            dp[i + 1][j + w] = min(dp[i][j] + 1, dp[i + 1][j + w])

min_value = inf
for i in range(n):
    if dp[i + 1][m] != inf:
        min_value = min(dp[i + 1][m], min_value)

if min_value == inf:
    print(-1)
else:
    print(min_value)
