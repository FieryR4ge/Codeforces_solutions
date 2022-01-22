import math

t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))

    print(math.ceil(sum(prices)/n))
