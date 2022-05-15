# -*- coding: utf-8 -*-

"""階段の問題に近い"""
if __name__ == "__main__":
    n = int(input())

    s = [None for _ in range(n)]
    for i in range(n):
        s[i] = input()

    # dp[i][j]: 上から i 番目、左から j 番目のマスにたどり着く方法の総数
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if s[i][j] == "#":
                continue

            top = i - 1
            left = j - 1

            if 0 <= top and s[top][j] == ".":
                dp[i][j] += dp[top][j]
            if 0 <= left and s[i][left] == ".":
                dp[i][j] += dp[i][left]

    print(dp[n-1][n-1])
