for _ in range(int(input())):
    n = input()
    k = len(n)
    n = int(n)
    p = int("1"*k)
    print(n//p)
    a = n//p + 9 * (k-1)
    print(a)