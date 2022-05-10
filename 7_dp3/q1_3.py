# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    dp = [None] * (n+1)  # dp[i]: i 番目の階段にたどり着く方法の数

    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        # i 段目にたどり着く方法の数は、
        # （１つ前の段にたどり着く方法）＋（２つ前の段にたどりつく方法）になる。
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n])
