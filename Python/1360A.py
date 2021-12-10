t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    c = min(a, b)
    c *= 2
    c = max(a, b, c)
    print(c*c)
