numbers = list(map(int, input().split()))

big = min(numbers[0], numbers[2], numbers[3])
small = min(numbers[1], numbers[0] - big)

print(256 * big + small * 32)
