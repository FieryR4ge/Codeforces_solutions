n = int(input())

for _ in range(n):
    length = int(input())
    numbers = list(map(int, input().split()))
    sorted_numbers = sorted(numbers)
    for i in range(length):
        if sorted_numbers[1] != numbers[i]:
            print(i+1)
