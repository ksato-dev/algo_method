# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())

    a_table = [None for _ in range(n)]
    for i in range(n):
        a_table[i] = [int(v) for v in input().split()]

    # dp[i][j]: 上から i 番目、左から j 番目のマスまで通ったときのスコアの最大値
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            top = i - 1
            left = j - 1
            cand_pre_dp = 0
            if 0 <= top:
                cand_pre_dp = max(dp[top][j], cand_pre_dp)
            if 0 <= left:
                cand_pre_dp = max(dp[i][left], cand_pre_dp)

            dp[i][j] = cand_pre_dp + a_table[i][j]

    print(dp[n-1][n-1])
