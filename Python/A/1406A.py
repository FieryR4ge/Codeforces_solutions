for _ in range(int(input())):
    t = int(input())
    a = 0
    b = 0
    for i in sorted(map(int, input().split())):
        if i == a:
            a += 1
        elif i == b:
            b += 1

    print(a + b)
