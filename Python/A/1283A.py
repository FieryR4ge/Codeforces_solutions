t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print(((23-a) * 60) + (60-b))
