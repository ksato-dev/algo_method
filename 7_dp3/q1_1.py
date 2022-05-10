# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, x, y = [int(v) for v in input().split()]
    a_list = [None] * n  # a_list[i]: i 番目の値

    a_list[0] = x
    a_list[1] = y
    for i in range(2, n):
        a_list[i] = (a_list[i-1] + a_list[i-2]) % 100

    print(a_list[n-1])
