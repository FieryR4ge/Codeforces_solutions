numbers = list(map(int, input().split()))

max_value = max(numbers)
numbers.remove(max_value)

for number in numbers:
    print(max_value-number)