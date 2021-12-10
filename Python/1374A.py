n = int(input())

for i in range(n):
    x, y, n = map(int, input().split())
    t = n % x
    if t > y:
        print(n - t + y)
    elif t == y:
        print(n)
    elif t < y:
        print(n - t - x + y)
