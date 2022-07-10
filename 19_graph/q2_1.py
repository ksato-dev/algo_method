
n, x = [int(v) for v in input().split()]
a_list = [int(v) for v in input().split()]

v = x
depth = 0
while v > 0:
    v = a_list[v - 1]
    depth += 1
    
print(depth)
