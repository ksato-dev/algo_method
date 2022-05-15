# -*- coding: utf-8 -*-

"""階段の問題に近い"""

if __name__ == "__main__":
    n = int(input())
    # dp[i][j]: (i, j) マスに到達する方法の総数
    dp = [[0] * n for _ in range(n)]

    # ０行目と０列目は１通りしか無いはず。
    dp[0][0] = 1

    # もらう DP で実装
    for i in range(n):
        for j in range(n):

            # 上と左を見に行けば一つ前の状態がわかる。
            top = i - 1
            left = j - 1

            if 0 <= top:
                dp[i][j] += dp[top][j]
            if 0 <= left:
                dp[i][j] += dp[i][left]

    print(dp[n-1][n-1])
