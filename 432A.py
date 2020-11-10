n, k = [int(i) for i in input().split()]
y = [int(i) for i in input().split() if int(i) <= 5 - k]
print(y)
print(len(y) // 3)