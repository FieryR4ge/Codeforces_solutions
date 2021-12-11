a = list(map(int, input().split()))

for i in range(a[1]):
    if str(a[0]).endswith('0'):
        a[0] //= 10
    else:
        a[0] -= 1

print(a[0])
