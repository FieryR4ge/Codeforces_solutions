t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    print(m * min(2, n-1))
