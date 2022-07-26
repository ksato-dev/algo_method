
n, m = [int(v) for v in input().split()]
w_list = [int(v) for v in input().split()]
v_list = [int(v) for v in input().split()]

# dp[i][j] := i 個のボール（0~i-1）を使って、重さ j にしたときの価値の最大値
# dp[i][j] == -1 の時、i 個のボールの組み合わせで j の重さが作れないとする。
dp = [[-1] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0

# 配る DP
max_value = -1
for i in range(n):
    w = w_list[i]
    v = v_list[i]
    for j in range(m):
        if dp[i][j] == -1:
            continue

        # 選ばない時
        dp[i + 1][j] = max(dp[i][j], dp[i + 1][j])
        cand_max_value1 = dp[i + 1][j]

        # 選ぶ時
        cand_max_value2 = 0
        if j + w <= m:
            dp[i + 1][j + w] = max(dp[i][j] + v, dp[i + 1][j])
            cand_max_value2 = dp[i + 1][j + w]

        max_value = max(max_value, max(cand_max_value1, cand_max_value2))

print(max_value)
