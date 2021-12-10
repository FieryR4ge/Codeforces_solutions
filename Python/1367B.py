t = int(input())

for i in range(t):
    n = int(input())
    even = 0
    odd = 0

    numbers = list(map(int, input().split()))

    for index, value in enumerate(numbers):
        if int(index % 2 != value % 2):
            if index % 2 == 0:
                even += 1
            else:
                odd += 1

    print(even if even == odd else -1)
