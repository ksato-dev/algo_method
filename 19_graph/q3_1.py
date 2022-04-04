# -*- coding: utf-8 -*-
"""Draw nodes."""


def draw_close_nodes():
    """hoge."""
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a_i, b_i = map(int, input().split())
        graph[a_i].append(b_i)
        graph[b_i].append(a_i)

    pre_node_list = []
    visited_node_list = [False for _ in range(n)]
    for k in range(n):
        if k == 0:
            visited_node_list[0] = True
            pre_node_list = [0]
            print(0)
            continue

        node_list = []
        while len(pre_node_list) > 0:
            node_id = pre_node_list.pop(0)
            for adj_node_id in graph[node_id]:
                if visited_node_list[adj_node_id]:
                    continue
                visited_node_list[adj_node_id] = True
                node_list.append(adj_node_id)
        node_list.sort()
        pre_node_list = node_list
        if len(node_list) > 0:
            node_list = [str(node_id) for node_id in node_list]
            print(' '.join(node_list))


if __name__ == '__main__':
    draw_close_nodes()
