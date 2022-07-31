n, m = [int(v) for v in input().split()]
a_list = [int(v) for v in input().split()]
b_list = [int(v) for v in input().split()]

ans = 0
for i, b in enumerate(b_list):
    delete_j = -1
    for j, a in enumerate(a_list):
        if a <= b:
            ans += 1
            delete_j = j
            break
    if delete_j != -1:
        a_list.pop(delete_j)

print(ans)
