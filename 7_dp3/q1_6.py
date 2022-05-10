# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    d_list = [int(v) for v in input().split()]

    dp = [False] * (n+1)  # dp[i]: i 番目のマスにたどり着くことが可能かどうか
    dp[0] = True

    for i in range(0, n+1):
        for j in range(0, m):
            d = d_list[j]
            next_id = d + i
            if next_id > n:
                continue
            if dp[i]:
                dp[next_id] = True

    if dp[n]:
        print("Yes")
    else:
        print("No")
