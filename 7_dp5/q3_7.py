
n = int(input())
w_list = [int(v) for v in input().split()]

# dp[i][j] := i 個のボールを２つの箱に振り分けた時、箱の重さの差が j かどうか
max_sum_w = 50 * 1000 + 1
dp = [[False] * max_sum_w for _ in range(n + 1)]  # ボール得るたびに差を取れば、１０００を超える事はないはず。
dp[0][0] = True

for i in range(n):
    w = w_list[i]
    for j in range(max_sum_w):
        if not dp[i][j]:
            continue

        # 重さが大きい箱へ振り分ける場合
        dp[i + 1][j + w] = True

        # 重さが小さい箱へ振り分ける場合
        diff_bw_boxes = abs(j - w)
        dp[i + 1][diff_bw_boxes] = True

min_diff = 10 ** 10

for j in range(max_sum_w):
    if dp[n][j]:
        min_diff = j
        break
    
print(min_diff)
