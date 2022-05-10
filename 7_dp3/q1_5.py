# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    a_list = [int(v) for v in input().split()]

    dp = [None] * n  # dp[i]: i 番目のマスにたどり着くまでの最短時間

    dp[0] = 0
    inf_val = 10 ** 8
    for i in range(1, n):
        min_cand_dp = inf_val

        # j 個前のマスから i 番目のマス（今見ているマス）に移動する。
        for j in range(1, m+1):
            k = i - j
            if k < 0:
                continue
            cand_dp = dp[k] + j * a_list[i]
            min_cand_dp = min(cand_dp, min_cand_dp)
        # dp[i] = min(min_cand_dp, dp[i])
        dp[i] = min_cand_dp

    print(dp[n-1])
