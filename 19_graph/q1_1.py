# -*- coding: utf-8 -*-
"""Q1-1. friend."""

if __name__ == '__main__':
    n_a_b_str = input()
    N, A, B = map(int, n_a_b_str.split())
    # print(N, A, B)

    # 入力
    G = [[False] * N for i in range(N)]
    for a in range(N):
        relationship = input()
        for b, o_or_x in enumerate(relationship):
            # 頂点 A から頂点 B への辺を張る
            if o_or_x == 'o':
                G[a][b] = True

                # 無向グラフの場合は次も実施
                G[b][a] = True

    if (G[A][B] and G[B][A]):
        print('Yes')
    else:
        print('No')
