
n, m = [int(v) for v in input().split()]
d_list = [int(v) for v in input().split()]

pos_list = [False] * (n + 1)
pos_list[0] = True

for i in range(n + 1):
    if not pos_list[i]:
        continue

    for j in range(m):
        d = d_list[j]
        next_i = d + i
        if next_i <= n:
            pos_list[next_i] = True

if pos_list[n]:
    print("Yes")
else:
    print("No")
