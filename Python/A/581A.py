a, b = map(int, input().split())

if a >= b:
    a -= b
    a //= 2
    print(f"{b} {a}")
else:
    b -= a
    b //= 2
    print(f"{a} {b}")
