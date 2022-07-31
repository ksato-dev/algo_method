x = int(input())
a_list = [int(v) for v in input().split()]
v_list = [50, 10, 5, 1]

num_coins = 0
for i in range(4):
    v = v_list[i]
    for j in range(a_list[i]):
        if x >= v:
            x -= v
            num_coins += 1
        else:
            break

print(num_coins)
