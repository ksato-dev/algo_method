x = int(input())
a_list = [int(v) for v in input().split()]
v_list = [50, 10, 5, 1]

total_num_coins = 0
for i in range(4):
    a = a_list[i]
    v = v_list[i]
    num_coins = x // v
    num_coins = min(num_coins, a)  # a で頭打ちする。
    total_num_coins += num_coins
    x -= v * num_coins

print(total_num_coins)
