# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())
    a_list = list(map(int, input().split()))
    time_list = [0] * n  # 各マスに到達するまでに必要な最短時間
    time_list[0] = 0
    time_list[1] = a_list[1]

    for n_id in range(2, n):
        candidate_time1 = a_list[n_id] + time_list[n_id-1]
        candidate_time2 = a_list[n_id] * 2 + time_list[n_id-2]
        time_list[n_id] = min(candidate_time1, candidate_time2)

    print(time_list[n-1])
