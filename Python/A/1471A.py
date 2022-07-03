import math

for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f"{math.ceil(sum(arr) / x)} {sum(math.ceil(i / x) for i in arr)}")
