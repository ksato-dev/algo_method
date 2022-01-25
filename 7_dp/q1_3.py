# -*- coding: utf-8 -*-
"""method of raising stairs."""

if __name__ == '__main__':
    n = int(input())

    # i 段目に到達するための方法の個数
    count_list = [0] * (n+1)
    count_list[0] = 1
    count_list[1] = 1

    for stair_num in range(2, n+1):
        count_list[stair_num] = count_list[stair_num-1] + \
            count_list[stair_num-2]

    print(count_list[n])
