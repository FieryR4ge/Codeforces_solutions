t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    if n > 2:
        result = (n-3) // x + 2
        print(result)
    else:
        print(1)
