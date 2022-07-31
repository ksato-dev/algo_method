n, m = [int(v) for v in input().split()]
a_list = [int(v) for v in input().split()]
b_list = [int(v) for v in input().split()]
a_used_list = [False for _ in range(n)]

ans = 0
for i, b in enumerate(b_list):
    for j, a in enumerate(a_list):
        if a_used_list[j]:
            continue

        if a <= b:
            ans += 1
            a_used_list[j] = True
            break

print(ans)
