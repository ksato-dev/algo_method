# -*- coding: utf-8 -*-
"""Q1-4. friend of friend."""


if __name__ == '__main__':
    n, m, x = map(int, input().split())

    graph = [[] for _ in range(n)]
    for edge_id in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    friends_of_friend = set()
    x_adj_nodes = graph[x]
    for b in x_adj_nodes:
        b_adj_nodes = graph[b]
        for c in b_adj_nodes:
            if c not in x_adj_nodes:
                friends_of_friend.add(c)

    ans_num = len(friends_of_friend)
    if x in friends_of_friend:
        print(ans_num - 1)
    else:
        print(ans_num)
