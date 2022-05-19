# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    a_list = [int(v) for v in input().split()]

    # dp[i][j] := (i, j) マスに行けるかどうか (bool)
    dp = [[False] * m for _ in range(n)]
    dp[0][0] = True  # 左上は必ず行ける。

    # 配る DP
    for i in range(n-1):
        a = a_list[i]
        for j in range(m):
            if not dp[i][j]:
                continue

            # 一個下に移動
            dp[i+1][j] = True

            # 一個下、Ai だけ右に移動
            next_j = j + a
            if next_j < m:
                dp[i+1][next_j] = True

    ans = sum([1 for flag in dp[n-1] if flag is True])
    print(ans)
