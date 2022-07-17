# -*- coding: utf-8 -*-

import queue

n, m = [int(v) for v in input().split()]

graph = [[] for _ in range(n)]
parent_tasks = [[] for _ in range(n)]

for i in range(m):
    f, s = [int(v) for v in input().split()]
    graph[f].append(s)
    parent_tasks[s].append(f)

finished_tasks = [False] * n

todo = queue.Queue()

# 依存０のタスクを登録。
for i in range(n):
    if len(parent_tasks[i]) == 0:
        todo.put(i)

while not todo.empty():
    curr_task = todo.get()
    finished_tasks[curr_task] = True

    for next_task in graph[curr_task]:
        if finished_tasks[next_task]:
            continue
        all_finished = True  # True のままなら next_task が依存している課題はない。
        for p_task in parent_tasks[next_task]:
            if not finished_tasks[p_task]:
                all_finished = False

        if all_finished:
            todo.put(next_task)
            
# print(finished_tasks)
if sum(finished_tasks) == n:
    print("Yes")
else:
    print("No")
