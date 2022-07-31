n = int(input())

period = 1
num_snacks = 1

# dp[i][j] := i 日間で作ったお菓子の数を j にできたかどうか
dp = [[False] * (n + 1) for _ in range(n + 1)]  # 最大 n 日間
dp[0][0] = True

for i in range(n):
    for j in range(n):
        if not dp[i][j]:
            continue

        # plan1
        dp[i + 1][j + 1] = True

        # plan2
        plan2_num_snacks = j * 3
        if plan2_num_snacks <= n:
            dp[i + 1][plan2_num_snacks] = True

ans = 0
for i in range(n + 1):
    if dp[i][n]:
        ans = i
        break

print(ans)
