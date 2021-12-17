t = int(input())

for _ in range(t):
    a = sorted(map(int, input().split()))
    if a[1] != a[2]:
        print("NO")
    else:
        print(f"YES \n{a[0]} {a[0]} {a[2]}")
