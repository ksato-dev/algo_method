# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n+1)  # i 番個埋める方法が何通りあるか
    dp[0] = 1
    dp[1] = 1

    # 樹形図を書くとイメージしやすい。
    if n > 1:
        dp[2] = 2
        for n_id in range(3, n+1):
            dp[n_id] = dp[n_id-1] + dp[n_id-2] + dp[n_id-3]

    print(dp[n])
