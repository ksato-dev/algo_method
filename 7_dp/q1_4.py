# -*- coding: utf-8 -*-
"""spreading tiles."""

if __name__ == '__main__':
    n = int(input())

    if n == 1:
        print(1)
        exit()

    # 長さ i に到達するための方法の個数
    count_list = [0] * (n+1)
    count_list[0] = 1
    count_list[1] = 1
    count_list[2] = 2

    for stair_num in range(3, n+1):
        count_list[stair_num] = count_list[stair_num-1] + \
            count_list[stair_num-2] + count_list[stair_num-3]

    print(count_list[n])
