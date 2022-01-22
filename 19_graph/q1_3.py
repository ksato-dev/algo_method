# -*- coding: utf-8 -*-
"""Q1-3. popular freand."""

if __name__ == '__main__':
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    max_num = 0
    max_id = 0
    for a in range(n):
        num_of_a_friends = len(graph[a])
        if max_num < num_of_a_friends:
            max_num = num_of_a_friends
            max_id = a

    graph[max_id].sort()
    out_str = ' '.join([str(b) for b in graph[max_id]])
    print(out_str)
