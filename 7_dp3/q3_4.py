# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    w_list = [int(v) for v in input().split()]  # 重さ
    v_list = [int(v) for v in input().split()]  # 価値

    # dp[i][j] := 0 ~ (i-1) までのボールを組み合わせたときのスコアの最大値
    dp = [[-1] * (m+1) for _ in range(n+1)]
    dp[0][0] = 0

    # 配る DP
    for i in range(n):
        w = w_list[i]
        v = v_list[i]
        for j in range(m+1):
            # 今の状態が None なら次に遷移できないので飛ばす（遷移できないはずはないが）
            if dp[i][j] == -1:
                continue

            # 選ばない時
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])

            # 次のボールを選ぶ時
            next_v = dp[i][j] + v
            next_w = j + w
            if next_w <= m:
                dp[i+1][next_w] = max(dp[i+1][next_w], next_v)

    print(max(dp[n]))  # n 個まで選んだときの最大値を出力
