# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    a_list = [int(v) for v in input().split()]  # 移動量
    b_list = [int(v) for v in input().split()]  # ポイント

    # dp[i][j] := (i, j) マスに来た時のスコアの最大値
    dp = [[-1] * m for _ in range(n)]

    dp[0][0] = 0

    for i in range(n-1):
        a = a_list[i]
        b = b_list[i]
        for j in range(m):
            # 今見てるところへ到達できなければ飛ばす
            if dp[i][j] == -1:
                continue

            # １段下へ
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])

            # １段下で右側へ
            next_right = j + a
            if next_right < m:
                dp[i+1][next_right] = max(dp[i+1][next_right], dp[i][j] + b)

    print(dp[n-1][m-1])
