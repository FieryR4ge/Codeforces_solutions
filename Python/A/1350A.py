t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    i = 2
    while n % i != 0:
        i += 1
    n += i + (k-1) * 2
    print(n)
