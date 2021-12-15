t = int(input())

for _ in range(t):
    a, b, c, n = map(int, input().split())
    x = a + b + c + n
    if (x % 3 == 0) and max(a, b, c) <= x//3:
        print("YES")
    else:
        print("NO")
