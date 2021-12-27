t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    x = list(map(int, input().split()))
    for i in x:
        if i % 2 == 1:
            count += 1

    if count == n:
        print("YES")
    else:
        print("NO")
