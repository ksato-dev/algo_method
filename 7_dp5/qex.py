n = int(input())
a_list = [int(v) for v in input().split()]
b_list = [int(v) for v in input().split()]
c_list = [int(v) for v in input().split()]
abc_list = list(zip(a_list, b_list, c_list))

# dp[i][j] := i 回目の試行で、j(a or b or c)を選んだ時の数値差の総和の最小値
inf = 10 ** 10
dp = [[inf] * 3 for _ in range(n + 1)]
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0

abc_pair_dict = {0: (1, 2), 1: (2, 0), 2: (0, 1)}

for i in range(n - 1):
    for j in range(3):
        if dp[i][j] == inf:
            continue
        
        temp_next_p = [0, 0, 0]
        for k in range(3):
            p = abc_list[i][j]
            next_p = abc_list[i + 1][k]
            add_value = abs(next_p - p)
            dp[i + 1][k] = min(dp[i][j] + add_value, dp[i + 1][k])
            

min_k = inf
for j in range(3):
    min_k = min(dp[n - 1][j], min_k)

print(min_k)
