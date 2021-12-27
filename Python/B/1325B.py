t = int(input())

for _ in range(t):
    n = int(input())

    numbers = set(map(int, input().split()))

    print(len(numbers))
