
n, m = [int(v) for v in input().split()]
w_list = [int(v) for v in input().split()]

# dp[i][j] := i 個のボール（0 ~ i - 1）で重さ j のボールを作れるかどうか。
dp = [[False] * (m + 1) for _ in range(n + 1)]

dp[0][0] = True

for i in range(n):
    w = w_list[i]
    for j in range(m + 1):
        if not dp[i][j]:
            continue

        # ボールを選ぶ・選ばないの場合を考える。
        # 選ばない時
        dp[i + 1][j] = True

        # 選ぶ時
        if w + j <= m:
            dp[i + 1][w + j] = True

ans = False
for i in range(n + 1):
    if dp[i][m]:
        ans = True

if ans:
    print("Yes")
else:
    print("No")
