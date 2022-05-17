# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    a_list = [int(v) for v in input().split()]  # 長さが N-2 なので注意。

    # dp[i][j]: 上から i 番目、左から j 番目のマスまで辿る方法の数
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    # 配る DP
    for i in range(n-1):
        for j in range(m):
            right = j + a_list[i]
            bottom = i + 1

            if bottom < n:
                dp[bottom][j] += dp[i][j]
                if right < m:
                    dp[bottom][right] += dp[i][j]

    # print(sum(dp[n-1]))  # 答えは最下段に到達する経路の総数ではない。
    ans = sum([1 for v in dp[n-1] if v > 0])
    print(ans)
