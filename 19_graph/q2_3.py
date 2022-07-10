import sys
sys.setrecursionlimit(10000)


def dfs(graph, node_id, visited, depth, depth_list):
    if visited[node_id]:
        depth_list[node_id] = depth
        return

    visited[node_id] = True

    adj_id_list = graph[node_id]
    for adj_id in adj_id_list:
        if not visited[adj_id]:
            depth_list[adj_id] = depth + 1
            dfs(graph, adj_id, visited, depth + 1, depth_list)


n = int(input())
p_list = [int(v) for v in input().split()]
graph = [list() for _ in range(n)]

for i in range(1, n):
    parent_node_id = p_list[i - 1]
    # 親から子へのエッジを貼れば良いらしい。
    # graph[i].append(parent_node_id)
    graph[parent_node_id].append(i)

visited = [False] * n
depth_list = [0] * n

depth_list[0] = 0
dfs(graph, 0, visited, depth_list[0], depth_list)

for i in range(n):
    print(depth_list[i])
