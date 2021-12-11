n = int(input())

for _ in range(n):
    k = int(input())

    s = sorted(map(int, input().split()))

    result = s[k-1] - s[0]

    for i in range(1, len(s)):
        result = min(result, s[i] - s[i-1])

    print(result)
