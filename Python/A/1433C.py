t = int(input())

for _ in range(t):
    n = int(input())
    aquarium = list(map(int, input().split()))
    index = -1
    max1 = max(aquarium)
    for i in range(n):
        if aquarium[i] != max1:
            continue
        if i > 0 and aquarium[i-1] != max1:
            index = i + 1
        if i < n - 1 and aquarium[i+1] != max1:
            index = i + 1

    print(index)