n = int(input())

period = 0

while n > 0:
    if n % 3:
        n -= 1
    else:
        n //= 3  # 割り切れるなら３で割る
    period += 1
    
print(period)
