n = list(map(int, input().split()))

a = '.' * (n[1] - 1)
b = '#'

for height in range(n[0]):
    if (height + 1) % 2 != 0:
        print("#" * n[1])
    else:
        print(f"{a}{b}")
        a, b = b, a
