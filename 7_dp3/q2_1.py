# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # a0, a1, a2, a3 = [int(v) for v in input().split()]

    # dp[i][j] := マス (i, j) における数値
    dp = [[None] * 4 for _ in range(4)]
    dp[0][0:4] = [int(v) for v in input().split()]

    for i in range(1, 4):
        for j in range(4):
            top = i - 1
            left = j - 1
            right = j + 1
            sum_values = 0
            sum_values += dp[top][j]
            if 0 <= left:
                sum_values += dp[top][left]
            if right < 4:
                sum_values += dp[top][right]
            dp[i][j] = sum_values

    print(dp[3][3])
