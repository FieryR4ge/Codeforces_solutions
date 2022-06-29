for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print("0 0")
    else:
        g = abs(a-b)
        m = min(a % g, g - a % g)
        print(f"{g} {m}")
