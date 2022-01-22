# -*- coding: utf-8 -*-
"""Q1-2. follow."""

if __name__ == '__main__':
    n_m_str = input()
    N, M = map(int, n_m_str.split())

    # 入力
    G = [[] for i in range(N)]
    for _ in range(M):
        relationship = input()
        a, b = map(int, relationship.split())
        # 頂点 A から頂点 B への辺を張る
        G[a].append(b)

    for a in range(N):
        adj_nodes = G[a]
        adj_nodes.sort()
        out_str = ' '.join([str(b) for b in adj_nodes])
        print(out_str)
