
import heapq
import sys
sys.setrecursionlimit(10000)


def dfs(graph, node_id, visited):
    if visited[node_id]:
        return
    visited[node_id] = True
    print(node_id, end=" ")

    for adj_node_id in graph[node_id]:
        if visited[adj_node_id]:
            continue
        dfs(graph, adj_node_id, visited)


n = int(input())
p_list = [int(v) for v in input().split()]

graph = [list() for _ in range(n)]
for i in range(n):
    heapq.heapify(graph[i])

for node_id in range(1, n):
    p = p_list[node_id - 1]
    heapq.heappush(graph[p], node_id)

visited = [False] * n
dfs(graph, 0, visited)
print()
