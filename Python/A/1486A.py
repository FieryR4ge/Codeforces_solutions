for _ in range(int(input())):
    n = int(input())
    need = 0
    have = 0
    enough = True

    arr = list(map(int, input().split()))

    for i in range(n):
        need += i
        have += arr[i]
        if need > have:
            enough = False

    print("YES" if enough else "NO")
