n = int(input())

for _ in range(n):
    t = int(input())

    orange = list(map(int, input().split()))
    chocolate = list(map(int, input().split()))

    min_orange = min(orange)
    min_chocolate = min(chocolate)

    counter = 0

    for o, c in zip(orange, chocolate):
        counter += max(o - min_orange, c - min_chocolate)

    print(counter)