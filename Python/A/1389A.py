t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    if l*2 <= r:
        print(f"{l} {l*2}")
    else:
        print("-1 " * 2)
