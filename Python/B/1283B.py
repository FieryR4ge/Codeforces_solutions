for _ in range(int(input())):
    n, k = map(int, input().split())
    result = n - n % k
    result += min(n % k, int(k / 2))
    print(result)
