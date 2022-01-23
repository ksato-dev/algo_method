# -*- coding: utf-8 -*-
"""array of numbers."""

if __name__ == "__main__":
    n, a0, a1 = map(int, input().split())
    a_list = [None] * n
    a_list[0] = int(a0)
    a_list[1] = int(a1)

    for a_id in range(2, n):
        a_list[a_id] = (a_list[a_id-1] + a_list[a_id-2]) % 100

    print(a_list[n-1])
