t = int(input())

for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))

    last = numbers[0]
    counter = 0

    for i in range(1, len(numbers)):
        new_value = numbers[i]
        a = min(new_value, last)
        b = max(new_value, last)
        while a * 2 < b:
            counter += 1
            a *= 2
        last = new_value

    print(counter)
