import math

n = int(input())

point_list = list()

for i in range(n):
    x, y = [int(v) for v in input().split()]
    point_list.append((x, y))

visited_list = [False for _ in range(n)]

# forward
point0 = point_list[0]
curr_point = point0
curr_point_id = 0
visited_list[curr_point_id] = True
total_dist = 0
for i in range(n - 1):
    min_dist = 10 ** 10
    min_dist_j = -1
    next_point = None

    # 距離が同じ時、若い順で取りたいので reversed する。
    for j in reversed(range(n)):
        if visited_list[j]:
            continue
        cand_next_point = point_list[j]
        dist = math.dist(curr_point, cand_next_point)
        if min_dist >= dist:
            next_point = cand_next_point
            min_dist = dist
            min_dist_j = j
    
    if min_dist_j != -1:
        total_dist += min_dist
        curr_point = next_point
        curr_point_id = min_dist_j
        visited_list[curr_point_id] = True

total_dist += math.dist(curr_point, point0)

print(total_dist)
