# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, m = [int(v) for v in input().split()]
    w_list = [int(v) for v in input().split()]

    # dp[i][j]: 0 ~ (i-1) 番のボールを組み合わせたときに重さ j となるかどうか。
    dp = [[False] * (m+1) for _ in range(n+1)]  # 全て選ばない状態も考えるので n+1 にする。

    # 初期化
    dp[0][0] = True  # 何も選ばない時、重さは０になる。

    # 配る DP
    for i in range(n):
        # 重さ 1 以上を見れば良い。
        for j in range(m+1):
            # 今見てる状態にたどり着けなければその先にも行けない。
            if not dp[i][j]:
                continue

            # 次のボールを選ばなければ無条件でひとつ下に遷移できる。
            dp[i+1][j] = True

            # 次のボールを選んだ時、今の重さに次のボールの重さを足した重さの状態に遷移する。
            next_w = j + w_list[i]  # 次のボールを加算した重さ
            if next_w <= m:
                dp[i+1][next_w] = True

    if dp[n][m]:
        print("Yes")
    else:
        print("No")
