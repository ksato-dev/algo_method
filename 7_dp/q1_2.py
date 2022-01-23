# -*- coding: utf-8 -*-
"""movement of cell."""

if __name__ == '__main__':
    n = int(input())
    a_list = list(map(int, input().split()))
    min_time_list = [0] * n

    min_time_list[1] = a_list[1]

    for cell_id in range(2, n):
        min_time_list[cell_id] = min(
            a_list[cell_id] + min_time_list[cell_id-1],
            a_list[cell_id] * 2 + min_time_list[cell_id-2])

    print(min_time_list[n-1])
