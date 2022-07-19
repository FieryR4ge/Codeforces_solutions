for _ in range(int(input())):
    n, m = map(int, input().split())
    answer = "NO"
    for i in range(n):
        a, b = map(int, input().split())
        c, d = map(int, input().split())
        if c == b and not m & 1:
            answer = "YES"

    print(answer)