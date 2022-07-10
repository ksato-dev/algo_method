import sys
sys.setrecursionlimit(10000)


def dfs(graph, node_id, visited):
    if visited[node_id]:
        return
    visited[node_id] = True
    print(node_id, end=" ")

    adj_id_list = graph[node_id]
    for adj_id in adj_id_list:
        if adj_id >= 0:
            dfs(graph, adj_id, visited)


n = int(input())
p_list = [int(v) for v in input().split()]
graph = [list() for _ in range(n)]

for i in range(1, n):
    parent_node_id = p_list[i - 1]
    graph[i].append(parent_node_id)
    graph[parent_node_id].append(i)

visited = [False] * n

dfs(graph, 0, visited)
print()
