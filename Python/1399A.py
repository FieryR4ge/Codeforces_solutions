for i in range(int(input())):
    n = int(input())
    a = set(map(int, input().split()))
    print('YES' if max(a)-min(a) < len(a) else 'NO')
