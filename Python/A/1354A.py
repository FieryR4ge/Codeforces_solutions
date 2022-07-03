t = int(input())

for _ in range(t):
    a, b, c, d = map(int, input().split())
    if b >= a:
        print(b)
        continue
    if c <= d:
        print("-1")
        continue
    a -= b
    time_to_sleep = c - d
    print(b + (a + time_to_sleep - 1) // time_to_sleep * c)
