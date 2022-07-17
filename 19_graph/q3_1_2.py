
n, m = [int(v) for v in input().split()]

graph = [list() for _ in range(n)]

for i in range(m):
    a, b = [int(v) for v in input().split()]
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(n)]
visited_nodes = [[] for _ in range(n)] 

for k in range(n):
    if k == 0:
        visited[k] = True
        visited_nodes[k].append(k)
        continue

    for visited_node in visited_nodes[k - 1]:
        for adj_node in graph[visited_node]:
            if visited[adj_node]:
                continue
            visited[adj_node] = True
            visited_nodes[k].append(adj_node)

for nodes in visited_nodes:
    nodes.sort()
    if len(nodes):
        print(*nodes)
