for _ in range(int(input())):
    n = int(input())
    pow = 1
    result = n * (n + 1) // 2
    while pow <= n:
        pow *= 2
    print(result - 2 * pow + 2)
