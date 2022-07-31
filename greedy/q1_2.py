n = int(input())

period = 0
while n > 0:
    if n % 2 == 0:
        n = n // 2
    else:
        n -= 1
    period += 1

print(period)
