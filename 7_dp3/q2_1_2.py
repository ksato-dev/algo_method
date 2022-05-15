# -*- coding: utf-8 -*-

if __name__ == "__main__":
    dp = [[None] * 4 for _ in range(4)]  # dp[i][j]: (i, j) マスの値
    dp[0] = [int(v) for v in input().split()]

    for i in range(1, 4):
        for j in range(4):
            top = i - 1
            left = j - 1
            right = j + 1
            exist_left = 0 <= left
            exist_right = right < 4

            sum_value = dp[top][j]
            if exist_left:
                sum_value += dp[top][left]
            if exist_right:
                sum_value += dp[top][right]

            dp[i][j] = sum_value

    print(dp[3][3])
