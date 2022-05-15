# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())

    a_table = [None for _ in range(n)]
    for i in range(n):
        a_table[i] = [int(v) for v in input().split()]

    # dp[i][j]: 上から i 番目、左から j 番目のマスまで通ったときのスコアの最小値
    inf_value = 10 ** 8
    dp = [[inf_value] * n for _ in range(n)]

    for i in range(n):
        for j in reversed(range(n)):
            if i == 0 and j == n-1:
                dp[i][j] = a_table[i][j]  # 右上のマスのスコア
                continue

            cand_pre_dp = inf_value
            top = i - 1
            right = j + 1
            if 0 <= top:
                cand_pre_dp = min(dp[top][j], cand_pre_dp)
            if right < n:
                cand_pre_dp = min(dp[i][right], cand_pre_dp)

            dp[i][j] = cand_pre_dp + a_table[i][j]

    print(dp[n-1][0])  # 左下のスコア。添字に注意ｗ
