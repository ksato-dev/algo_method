# -*- coding: utf-8 -*-
"""movement of cell(2)."""

if __name__ == '__main__':
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))

    min_time_list = [0] * n

    inf = 10**10
    for cell_id in range(1, n):
        min_time = inf
        for m_id in range(1, m+1):
            if cell_id - m_id < 0:
                continue
            min_time = min(a_list[cell_id] * m_id +
                           min_time_list[cell_id - m_id], min_time)

        min_time_list[cell_id] = min_time

    print(min_time_list[n-1])
