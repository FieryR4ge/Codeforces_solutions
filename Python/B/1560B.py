t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    n = 2 * abs(a-b)
    if a > n or b > n or c > n:
        print("-1")
    else:
        if c > n//2:
            print(c-n//2)
        else:
            print(c+n//2)
