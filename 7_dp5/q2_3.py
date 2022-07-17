
n = int(input())
pay_table = [None] * n
for i in range(n):
    pay_table[i] = [int(v) for v in input().split()]

# dp[i][j] := i 日目に j の仕事を実施したときの報酬の最大値
dp = [[0] * 3 for _ in range(n)]
dp[0][0] = pay_table[0][0]
dp[0][1] = pay_table[0][1]
dp[0][2] = pay_table[0][2]

# 直前のタスク番号のテーブルを作る
pre_tasks_dict = {0:[1, 2], 1:[0, 2], 2:[0, 1]}  # {curr_id: pre_id_list, ...}

for i in range(1, n):
    for j in range(3):
        id0 = pre_tasks_dict[j][0]
        id1 = pre_tasks_dict[j][1]
        dp[i][j] = max(dp[i - 1][id0], dp[i - 1][id1]) + pay_table[i][j]

print(max(dp[n - 1]))
