
n, x, y = [int(v) for v in input().split()]

a_list = [0] * n
a_list[0] = x
a_list[1] = y

for i in range(2, n):
    a_list[i] = (a_list[i-1] + a_list[i-2]) % 100

print(a_list[n-1])
