# -*- coding: utf-8 -*-

import queue

n, m = [int(v) for v in input().split()]

graph = [[] * m for _ in range(n)]

for i in range(m):
    a, b = [int(v) for v in input().split()]
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * n

todo = queue.Queue()
todo.put(0)
dist[0] = 0

while not todo.empty():
    curr_student = todo.get()

    friends = graph[curr_student]
    for student in friends:
        if dist[student] != -1:
            continue
        dist[student] = dist[curr_student] + 1
        todo.put(student)
    
print(max(dist))
