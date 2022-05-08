# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n, x, y = map(int, input().split())
    a_list = [-1] * n
    a_list[0] = x
    a_list[1] = y

    for n_id in range(2, n):
        a_list[n_id] = (a_list[n_id-1] + a_list[n_id-2]) % 100

    print(a_list[n-1])
