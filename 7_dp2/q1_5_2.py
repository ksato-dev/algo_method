# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    inf_time = 10**8
    dp = [inf_time] * n
    dp[0] = 0

    for i in range(n):
        for j in range(1, m+1):
            dp[i] = min(dp[i], dp[i-j] + j * a_list[i])

    print(dp[n-1])
