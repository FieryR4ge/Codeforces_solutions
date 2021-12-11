a = int(input())

answers = []

for i in range(a):
    numbers = list(map(int, input().split()))
    counter = 0

    if numbers[0] % numbers[1] == 0:
        print(0)
    else:
        print(numbers[1] - numbers[0] % numbers[1])

for answer in answers:
    print(answer)
