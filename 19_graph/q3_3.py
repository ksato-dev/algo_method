
import queue

h, w = [int(v) for v in input().split()]
x0, y0, x1, y1 = [int(v) for v in input().split()]

s_map = [None] * h
for i in range(h):
    s_map[i] = input()

dist = [[-1] * w for _ in range(h)]

todo = queue.Queue()
todo.put((x0, y0))
dist[x0][y0] = 0

move_vector = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# cnt = 0
while not todo.empty():
    # cnt += 1
    curr_cell = todo.get()
    # print(curr_cell)
    curr_i = curr_cell[0]
    curr_j = curr_cell[1]

    for mvec in move_vector:
        # print(adj_cell)
        next_i = curr_i + mvec[0]
        next_j = curr_j + mvec[1]
        if not (0 <= next_i < h):
            continue
        if not (0 <= next_j < w):
            continue
        if s_map[next_i][next_j] == "B":
            continue

        # 探索済みなら飛ばす操作を絶対入れる。
        if dist[next_i][next_j] != -1:
            continue

        dist[next_i][next_j] = dist[curr_i][curr_j] + 1
        todo.put((next_i, next_j))

print(dist[x1][y1])
# print("cnt:", cnt)
