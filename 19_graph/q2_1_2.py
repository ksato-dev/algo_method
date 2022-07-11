def dfs(graph, node_id, tgt_node_id, visited, depth_list):
    if visited[node_id]:
        return
    visited[node_id] = True

    if node_id == tgt_node_id:
        return

    for adj_node_id in graph[node_id]:
        if visited[adj_node_id]:
            continue
        depth_list[adj_node_id] += 1 + depth_list[node_id]  # 親の深さ＋１
        dfs(graph, adj_node_id, tgt_node_id, visited, depth_list)


n, x = [int(v) for v in input().split()]
a_list = [int(v) for v in input().split()]

graph = [list() for _ in range(n)]
for node_id in range(1, n):
    parent_node_id = a_list[node_id - 1]
    graph[parent_node_id].append(node_id)
    # graph[node_id].append(parent_node_id)

visited = [False] * n
depth_list = [0] * n  # 参照渡ししたいでのリスト化する
dfs(graph, 0, x, visited, depth_list)

print(depth_list[x])
