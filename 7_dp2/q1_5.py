# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    inf_time = 10 ** 10
    dp = [inf_time] * n  # i 番目のマスにたどり着く方法の数
    dp[0] = 0

    # 頭が悪くて思いつかん。
    for i in range(1, n):
        for j in range(1, m+1):
            if i - j >= 0:
                curr_time = dp[i-j] + j * a_list[i]
                dp[i] = min(dp[i], curr_time)

    print(dp[n-1])
