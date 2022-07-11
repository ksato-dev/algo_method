
import sys
sys.setrecursionlimit(10000)


def dfs(chiled_node_id, tgt_parent_node_id, a_list, depth):
    if chiled_node_id == tgt_parent_node_id:
        return

    parent_node_id = a_list[chiled_node_id - 1]
    depth[0] += 1
    dfs(parent_node_id, tgt_parent_node_id, a_list, depth)


n, x = [int(v) for v in input().split()]
a_list = [int(v) for v in input().split()]

depth = [0]
dfs(x, 0, a_list, depth)

print(depth[0])
