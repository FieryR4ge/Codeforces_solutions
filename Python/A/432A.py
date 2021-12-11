n, k = map(int, input().split())
y = [int(i) for i in input().split() if int(i) <= 5 - k]
print(len(y) // 3)
