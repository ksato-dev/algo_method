# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    dp = [[None] * n for _ in range(n)]  # dp[i][j]: (i, j) マスの値
    dp[0] = [int(v) for v in input().split()]

    for i in range(1, n):
        for j in range(n):
            top = i - 1
            left = j - 1
            right = j + 1
            exist_left = 0 <= left
            exist_right = right < n

            sum_value = dp[top][j]
            if exist_left:
                sum_value += dp[top][left]
            if exist_right:
                sum_value += dp[top][right]

            dp[i][j] = sum_value % 100

    print(dp[n-1][n-1])
