# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    w_list = [int(v) for v in input().split()]

    # dp[i][j] := 0 ~ (i-1) までの i 個のボールを組み合わせて、j の重さにできるか。
    dp = [[False] * (m+1) for _ in range(n+1)]  # 添字を最大で n と m にしたい。
    dp[0][0] = True  # 何も選ばない時は重さが０

    # 配る DP
    for i in range(n):
        w = w_list[i]
        for j in range(m+1):
            if not dp[i][j]:
                continue

            # 選ばない時
            dp[i+1][j] = True

            # 選ぶ時
            next_w = j + w
            if next_w <= m:
                dp[i+1][next_w] = True

    ans = False
    for i in range(n+1):
        if dp[i][m]:
            ans = True
            break

    if ans:
        print("Yes")
    else:
        print("No")
