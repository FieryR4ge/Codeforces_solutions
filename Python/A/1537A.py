t = int(input())

for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))

    sum_numbers = sum(numbers)

    if sum_numbers < n:
        print(1)
    else:
        print(sum_numbers - n)
