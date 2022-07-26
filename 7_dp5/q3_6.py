
n, a, b = [int(v) for v in input().split()]
x_list = [int(v) for v in input().split()]

# dp[i][j] := i 個のカード（0~i-1）を使った合計値を A で割った余りが j となるかどうか
dp = [[False] * (a + 1) for _ in range(n + 1)]
dp[0][0] = True

exist_sum_mod_a_is_b = False

# 配る DP
for i in range(n):
    x = x_list[i]
    for j in range(a):
        if dp[i][j] == False:
            continue

        # カードを選ばない時
        dp[i + 1][j] = True

        # カードを選ぶ時
        sum_mod_a = (j + x) % a
        dp[i + 1][sum_mod_a] = True

if dp[n][b]:
    exist_sum_mod_a_is_b = True

ans = "Yes" if exist_sum_mod_a_is_b else "No"
print(ans)
