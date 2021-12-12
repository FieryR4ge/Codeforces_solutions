t = int(input())

for _ in range(t):
    w, h, n = map(int, input().split())
    parts = 1
    c = w * h
    while c % 2 == 0:
        c /= 2
        parts *= 2
    if parts >= n:
        print("YES")
    else:
        print("NO")
