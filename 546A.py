a = list(map(int, input().split()))

volume = [a[0]*i for i in range(1, a[2]+1)]

result = sum(volume) - a[1]
if result > 0:
    print(result)
else:
    print(0)
