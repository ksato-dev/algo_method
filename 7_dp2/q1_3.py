# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n+1)  # 階段の i 番目に到達する方法が何通りか
    dp[0] = 1
    dp[1] = 1

    for n_id in range(2, n+1):
        dp[n_id] = dp[n_id-1] + dp[n_id-2]

    print(dp[n_id])
