t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a_min = a.index(min(a))
    a_max = a.index(max(a))

    print(min(
        max(a_min, a_max) + 1,
        (n-1) - min(a_min, a_max) + 1,
        (n-1) - a_max + a_min + 2,
        (n-1) - a_min + a_max + 2
    ))
