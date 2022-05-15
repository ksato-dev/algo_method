# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    # dp[i][j]: i 番目のタスクで j 番取り組むときの最大値
    dp = [[None] * 3 for _ in range(n)]

    for i in range(n):
        a_list = [int(v) for v in input().split()]

        for j in range(3):
            a = a_list[j]

            if i == 0:
                dp[i][j] = a
                continue

            # 一つ前の値の中で最も大きいものを選ぶ。
            cand_pre_dp = 0
            for k in range(3):
                if j == k:
                    continue
                cand_pre_dp = max(cand_pre_dp, dp[i-1][k])

            dp[i][j] = cand_pre_dp + a

    ans = 0
    for j in range(3):
        ans = max(dp[n-1][j], ans)

    print(ans)
