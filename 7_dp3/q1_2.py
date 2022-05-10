# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    a_list = [int(v) for v in input().split()]

    dp = [None] * n  # dp[i]: i 番目のマスまでたどり着くのに必要な最短時間
    dp[0] = 0
    dp[1] = a_list[1]

    for i in range(2, n):
        cand_dp1 = dp[i-1] + a_list[i]
        cand_dp2 = dp[i-2] + 2 * a_list[i]
        dp[i] = min(cand_dp1, cand_dp2)

    print(dp[n-1])
