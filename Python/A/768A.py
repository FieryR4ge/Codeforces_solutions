t = int(input())
n = sorted(map(int, input().split()))
print(len(list(filter(lambda x: x != n[0] and x != n[-1], n))))
