# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    dp = [None] * (n+1)  # dp[i]: 横幅 i まで敷き詰める方法の数
    dp[0] = 1

    for i in range(1, n+1):
        if i == 1:
            # １通りしか無いはず。dp[1] = dp[0]
            dp[1] = 1
        elif i == 2:
            # ２通りしか無いはず。dp[2] = dp[1] + dp[0]
            dp[2] = 2
        elif i == 3:
            # ４通りしか無いはず。dp[3] = dp[2] + dp[1] + dp[0]
            dp[3] = 4
        else:
            # dp[4] 以降は、dp[i] = dp[i-1] + dp[i-2] + dp[i-3] となる。
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[n])
