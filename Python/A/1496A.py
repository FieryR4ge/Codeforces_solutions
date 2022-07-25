for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()

    if (s[:k] == s[-k:][::-1] and k < n / 2) or k == 0:
        print(s[:k])
        print(s[-k:][::-1])
        print(s[-k:])
        print("YES")
    else:
        print("NO")
